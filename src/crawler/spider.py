import string
import time
from unicodedata import normalize
from abc import ABC, abstractmethod
from typing import Generator, Any

import jieba
from bs4 import BeautifulSoup
from scrapy import Spider as Prototype, Request
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import SelectorList

from .models import Article
from ..kernel import Config, Database


class Spider(ABC, Prototype):
    _extractor = LinkExtractor()

    custom_settings = {
        'LOG_LEVEL': 'WARNING',
    }

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
    }
    FAKEUSERAGENT_PROVIDERS = [
        'scrapy_fake_useragent.providers.FakeUserAgentProvider',
        'scrapy_fake_useragent.providers.FakerProvider',
        'scrapy_fake_useragent.providers.FixedUserAgentProvider'
    ]
    USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) ' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/96.0.4664.93 ' \
                 'Safari/537.36'

    def __init__(self, config: Config):
        super().__init__()
        self.config = config
        self.database = Database(self.config)
        self.collection = self.database.get_collection("articles")

    @staticmethod
    def explode(text: str) -> filter:
        def remover_(s: str) -> bool:
            i = s.strip()
            return (i != "") and (i != "\n") and (i not in string.punctuation)

        text = normalize('NFKC', text)
        return filter(remover_, jieba.cut(text, use_paddle=True))

    @classmethod
    def explode_as_list(cls, text: str) -> list:
        return list(cls.explode(text))

    @staticmethod
    def clear_html_tags(text: str) -> str:
        return BeautifulSoup(text, "lxml").text

    @staticmethod
    def clear_syntax_from_selectors(selectors: SelectorList) -> str:
        return " ".join(filter(
            lambda i: i != "\n",
            " ".join(map(
                lambda s: s.strip(),
                selectors.extract()
            )).split("\n")
        ))

    @classmethod
    def clear_html_tags_from_selectors(cls, selectors: SelectorList) -> str:
        return cls.clear_html_tags(cls.clear_syntax_from_selectors(selectors))

    def storage_article(self, article: Article) -> None:
        article.captured_time = round(time.time())
        self.collection.insert_one(article.dict())

    @abstractmethod
    def capture(self, response: HtmlResponse) -> None:
        pass

    def parse(self, response: HtmlResponse, **kwargs) -> Generator[Request, Any, None]:
        for link in self._extractor.extract_links(response):
            yield Request(link.url, callback=self.parse)
        self.capture(response)
