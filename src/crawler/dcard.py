from scrapy.http import HtmlResponse

from .spider import Spider


class Dcard(Spider):
    name = "Dcard"
    allowed_domains = ['dcard.tw']
    start_urls = ["https://dcard.tw"]

    def capture(self, response: HtmlResponse) -> None:
        print(response)
