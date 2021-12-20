from multiprocessing import Process

from scrapy.crawler import CrawlerProcess

from .dcard import Dcard
from .gamer import Gamer
from .ptt import PTT
from ..kernel import Config


class Crawler(Process):
    crawlers = [PTT, Dcard, Gamer]

    def __init__(self, config: Config):
        super().__init__()
        self.config = config

    def run(self) -> None:
        process = CrawlerProcess()
        for do in self.crawlers:
            process.crawl(do, self.config)
        process.start()
