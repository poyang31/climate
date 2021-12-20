import string
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generator, Any, Union
from unicodedata import normalize

import jieba
from bs4 import BeautifulSoup
from scrapy import Spider as Prototype, Request
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import SelectorList

from .models import Article
from ..kernel import Config, Database

root_path = Path(__file__).parent.resolve()


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
        with open(f'{root_path}/../../explode_filter.txt', 'r') as f:
            self.stoplist = f.read().split("\n")

    def explode(self, text: str) -> filter:
        def remover_(s: str) -> bool:
            i = s.strip()
            return (i != "") and (i != "\n") and (i not in string.punctuation) and (i not in self.stoplist)

        text = normalize('NFKC', text)
        return filter(remover_, jieba.cut(text, cut_all=False))

    def explode_as_list(self, text: str) -> list:
        return list(self.explode(text))

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
    def capture(self, response: HtmlResponse) -> Union[Article, None]:
        pass

    def parse(self, response: HtmlResponse, **kwargs) -> Generator[Request, Any, None]:
        for link in self._extractor.extract_links(response):
            yield Request(link.url, callback=self.parse)
        article = self.capture(response)
        if article is not None:
            self.storage_article(article)
