import time
from collections import Counter
from multiprocessing import Process
from time import sleep
from typing import List

from pandas import DataFrame

from .models import Result
from ..crawler.models import Article
from ..kernel import Config, Database


class Analysis(Process):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

    @staticmethod
    def do(articles: List[Article]) -> List[Result]:
        all_words_unpacked = [j for i in articles for j in i.words]
        count = Counter(all_words_unpacked)
        common = count.most_common()
        data = DataFrame(common)
        return data.iloc[0:10]

    @staticmethod
    def storage_results(database: Database, results: List[Result]) -> None:
        def convert(result: Result) -> dict:
            result.captured_time = round(time.time())
            return result.dict()

        result_dicts = [convert(i) for i in results]
        results_collection = database.get_collection("results")
        results_collection.insert_many(result_dicts)

    def run(self) -> None:
        database = Database(self.config)
        articles_collection = database.get_collection("articles")
        if articles_collection.count_documents({}) < 10000:
            time.sleep(30)
            return self.run()
        articles = [Article.parse_obj(i) for i in articles_collection.find({})]
        self.storage_results(database, self.do(articles))
        sleep(300)
        self.run()
