import time
from collections import Counter
from multiprocessing import Process
from time import sleep
from typing import List

from pandas import DataFrame
from pymongo.collection import Collection

from .models import Result
from ..crawler.models import Article
from ..kernel import Config, Database


class Analysis(Process):
    def __init__(self, config: Config):
        super().__init__()
        self.config = config

    @staticmethod
    def common(articles: List[Article]) -> str:
        all_words_unpacked = [j for i in articles for j in i.words]
        count = Counter(all_words_unpacked)
        common = count.most_common()
        data = DataFrame(common)
        result: DataFrame = data.iloc[0:10]
        return result.to_json()

    @classmethod
    def do(cls, articles: List[Article]) -> List[Result]:
        tasks = {
            "common": cls.common
        }
        return [
            Result(name=i, content=j(articles))
            for i, j in tasks.items()
        ]

    @staticmethod
    def storage_results(database: Database, results: List[Result]) -> None:
        def convert(result: Result) -> dict:
            result.captured_time = round(time.time())
            return result.dict()

        result_dicts = [convert(i) for i in results]
        results_collection = database.get_collection("results")
        results_collection.insert_many(result_dicts)

    def execute(self, database: Database, articles_collection: Collection) -> None:
        if articles_collection.count_documents({}) > 10000:
            articles = [Article.parse_obj(i) for i in articles_collection.find({})]
            self.storage_results(database, self.do(articles))
            sleep(300)
        else:
            time.sleep(30)

    def run(self) -> None:
        database = Database(self.config)
        articles_collection = database.get_collection("articles")
        while True:
            self.execute(database, articles_collection)
