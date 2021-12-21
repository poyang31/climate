from re import fullmatch
from typing import Union

from scrapy.http import HtmlResponse

from .models import Article
from .spider import Spider
from ..kernel import Config


class PTT(Spider):
    name = "PTT"
    allowed_domains = ['www.ptt.cc']
    start_urls = ["https://www.ptt.cc/bbs/index.html"]

    COOKIES_ENABLED = True

    def __init__(self, config: Config):
        super().__init__(config)
        self.DOWNLOADER_MIDDLEWARES.update({
            'src.crawler.middlewares.ptt_cookies.CookiesMiddleware': 700
        })

    def capture(self, response: HtmlResponse) -> Union[Article, None]:
        # Get Full Title
        query = response.css("#main-content > div:nth-child(3) > span.article-meta-value")
        full_title = self.clear_html_tags_from_selectors(query)
        if full_title.strip() == "":
            return None
        title_data = fullmatch(r"\[(.*?)\](.*?)", full_title)
        # Get Tag and Title
        if title_data is None:
            tag = "Unknown"
            title = full_title
        else:
            tag = title_data.group(1)
            title = title_data.group(2)
        tag = tag.strip()
        title = title.strip()
        # Get Class
        query = response.css(
            "#main-content > div.article-metaline-right > span.article-meta-value")
        class_ = self.clear_html_tags_from_selectors(query)
        # Get Content
        query = response.xpath('//*[@id="main-content"]/text()[1]')
        content = self.clear_html_tags_from_selectors(query)
        # Get URL
        url = response.url
        # Get Words
        words = self.unique_filter(self.explode_as_list(content))
        # Get Times
        query = response.css("#main-content > div:nth-child(4) > span.article-meta-tag")
        if query is None:
            query = response.css("#main-content > div:nth-child(3) > span.article-meta-tag")
        if "時間" == self.clear_html_tags_from_selectors(query):
            query = response.css('#main-content > div:nth-child(4) > span.article-meta-value')
            if query is None:
                query = response.css("#main-content > div:nth-child(3) > span.article-meta-value")
            time_ = self.clear_html_tags_from_selectors(query)
            created_time = updated_time = self.human_to_unix_timestamp(time_[:24])
        elif "發信站" == self.clear_html_tags_from_selectors(query):
            query = response.css('#main-content > div:nth-child(4) > span.article-meta-value')
            if query is None:
                query = response.css("#main-content > div:nth-child(3) > span.article-meta-value")
            time_ = self.clear_html_tags_from_selectors(query)
            time_ = fullmatch(r"(.*?) \((.*?)\)", time_).group(2)
            created_time = updated_time = self.human_to_unix_timestamp(time_[:24])
        else:
            created_time = updated_time = -1
        # Return
        return Article(
            origin=self.name,
            class_=class_,
            tag=tag,
            title=title,
            content=content,
            url=url,
            words=words,
            created_time=created_time,
            updated_time=updated_time
        )
