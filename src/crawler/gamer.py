from re import fullmatch
from typing import Union

from scrapy.http import HtmlResponse

from .models import Article
from .spider import Spider


class Gamer(Spider):
    name = "Gamer"
    allowed_domains = ['forum.gamer.com.tw']
    start_urls = ["https://forum.gamer.com.tw"]

    def capture(self, response: HtmlResponse) -> Union[Article, None]:
        full_title = self.clear_html_tags_from_selectors(response.css("title"))
        title_data = fullmatch(r"【(.*?)】(.*?) @(.*?) (.*?)", full_title)
        if title_data is None:
            return None
        # Get Tag, Title and Class
        tag = title_data.group(1)
        title = title_data.group(2)
        class_ = title_data.group(3)
        # Get Content
        query = response.xpath('/html/body/div[5]/div/div[2]/section[2]/div[2]/div[2]/article/div')
        content = self.clear_html_tags_from_selectors(query)
        # Get URL
        url = response.url
        # Get Words
        words = self.explode_as_list(content)
        # Get Times
        query = response.xpath('/html/body/div[5]/div/div[2]/section[2]/div[2]/div[1]/div[3]/a')
        if query:
            query = query.extract()[0]
            updated_time = self.human_to_unix_timestamp(self.clear_html_tags(query)[:19])
        else:
            updated_time = -1
        query = response.xpath('/html/body/div[5]/div/div[2]/section[2]/div[2]/div[1]/div[3]/a/@data-mtime')
        if query:
            query = query.extract()[0]
            created_time = self.human_to_unix_timestamp(self.clear_html_tags(query)[:19])
        else:
            created_time = updated_time
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
