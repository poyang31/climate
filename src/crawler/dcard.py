import datetime
import time
from typing import Union

from scrapy.http import HtmlResponse

from .models import Article
from .spider import Spider


class Dcard(Spider):
    name = "Dcard"
    allowed_domains = ['dcard.tw']
    start_urls = ["https://dcard.tw"]

    def capture(self, response: HtmlResponse) -> Union[Article, None]:
        # Get Title
        query = response.css(
            "#__next > div.bvk29r-0.eFPEdc > div.bvk29r-2.etVvYS > div > div > div > div > article > div.sc-1eorkjw-1.ccTaOU > div > h1")
        title = self.clear_html_tags_from_selectors(query)
        if title.strip() == "":
            return None
        tag = "Unknown"
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
        words = self.unique_filter(self.explode_as_list(content))
        # Get Times
        query = response.xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div/div/div/article/div[2]/div[2]/text()')
        time_ = self.clear_html_tags_from_selectors(query)
        if time_:
            if "年" not in time_:
                current_time = datetime.datetime.now()
                time_ = f"{current_time.year}年{time_}"
            struct_time = time.strptime(time_, "%Y年%m月%d日 %H:%M")
            time_stamp = round(time.mktime(struct_time))
            created_time = updated_time = time_stamp
        else:
            raise Exception("Time is not exists")
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
            updated_time=updated_time,
        )
