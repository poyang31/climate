from scrapy.http import HtmlResponse

from .spider import Spider


class Gamer(Spider):
    name = "Gamer"
    allowed_domains = ['forum.gamer.com.tw']
    start_urls = ["https://forum.gamer.com.tw"]

    def capture(self, response: HtmlResponse) -> None:
        print(response)
