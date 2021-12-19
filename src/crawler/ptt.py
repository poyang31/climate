from re import fullmatch

from dateutil.parser import parse
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

    def capture(self, response: HtmlResponse) -> None:
        # Get Full Title
        query = response.css("#main-content > div:nth-child(3) > span.article-meta-value")
        full_title = self.clear_html_tags_from_selectors(query)
        if full_title.strip() != "":
            title_data = fullmatch(r"\[(.*?)\](.*?)", full_title)
            # Get Tag and Title
            if title_data is None:
                tag = "Unknown"
                title = full_title
            else:
                tag = title_data.group(1)
                title = title_data.group(2)
            # Get Class
            query = response.css("#main-content > div.article-metaline-right > span.article-meta-value")
            class_ = self.clear_html_tags_from_selectors(query)
            # Get Content
            query = response.xpath('//*[@id="main-content"]/text()[1]')
            content = self.clear_html_tags_from_selectors(query)
            # Get URL
            url = response.url
            # Get Words
            words = self.explode_as_list(content)
            # Get Times
            query = response.css('#main-content > div:nth-child(4) > span.article-meta-value')
            time_ = self.clear_html_tags_from_selectors(query)
            created_time = updated_time = round(parse(time_).timestamp())
            # Storage
            self.storage_article(Article(
                origin=self.name,
                class_=class_,
                tag=tag,
                title=title,
                content=content,
                url=url,
                words=words,
                created_time=created_time,
                updated_time=updated_time
            ))