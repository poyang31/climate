from re import fullmatch
import time
import datetime
from dateutil.parser import parse
from scrapy.http import HtmlResponse
from .models import Article
from .spider import Spider
from ..kernel import Config


class Dcard(Spider):
    name = "Dcard"
    allowed_domains = ['dcard.tw']
    start_urls = ["https://dcard.tw"]

    def __init__(self, config: Config):
        super().__init__(config)
        self.DOWNLOADER_MIDDLEWARES.update({
            'src.crawler.middlewares.ptt_cookies.CookiesMiddleware': 700
        })

    def capture(self, response: HtmlResponse) -> None:
        # Get Full Title
        query = response.css("#__next > div.bvk29r-0.eFPEdc > div.bvk29r-2.etVvYS > div > div > div > div > article > div.sc-1eorkjw-1.ccTaOU > div > h1")
        full_title = self.clear_html_tags_from_selectors(query)
        tag = "NONE"
        title = full_title
        # Get Class
        query = response.css(
            "#__next > div.bvk29r-0.eFPEdc > div.bvk29r-2.etVvYS > div > div > div > div > article > div.sc-1eorkjw-3.jJbLey > div:nth-child(1) > a")
        class_ = self.clear_html_tags_from_selectors(query)
        # Get Content
        query = response.css(
            '#__next > div.bvk29r-0.eFPEdc > div.bvk29r-2.etVvYS > div > div > div > div > article > div.sc-1eorkjw-5.hKSyLQ > div')
        content = self.clear_html_tags_from_selectors(query)
        # Get URL
        url = response.url
        # Get Words
        words = self.explode_as_list(content)

        # Get Times
        query = response.xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div/div/div/article/div[2]/div[2]/text()')
        time_ = self.clear_html_tags_from_selectors(query)
        if len(time_) == 17:
            struct_time = time.strptime(time_, "%Y年%m月%d日 %H:%M")  # 轉成時間元組
            time_stamp = int(time.mktime(struct_time))  # 轉成時間戳
            created_time = time_stamp
        elif len(time_) == 12:
            currentDateTime = datetime.datetime.now()  # 抓現在時間
            date = currentDateTime.date()
            year = date.strftime("%Y")  # 抓出年
            time_ = year+"年"+time_  # 年分+時間合併
            struct_time = time.strptime(time_, "%Y年%m月%d日 %H:%M")  # 轉成時間元組
            time_stamp = int(time.mktime(struct_time))  # 轉成時間戳
            created_time = time_stamp
        else:
            created_time = 0
            updated_time = 0
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
            updated_time=updated_time,
        ))
