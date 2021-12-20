from scrapy.http import HtmlResponse

from src.crawler.spider import Spider


class FakeCrawler(Spider):
    name = "Test"

    def capture(self, response: HtmlResponse) -> None:
        return None
