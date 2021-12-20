from collections import Counter
from pathlib import Path

from matplotlib.pyplot import savefig
from pandas import DataFrame

from ..crawler.models import Article
from ..kernel import Config, Database

current_path = Path(__file__).parent.resolve()
config = Config()
database = Database(config)


def test_rank():
    articles_collection = database.get_collection("articles")
    articles = [Article.parse_obj(i) for i in articles_collection.find({})]
    all_words_unpacked = [j for i in articles for j in i.words]
    count = Counter(all_words_unpacked)
    common = count.most_common()
    df = DataFrame(common)
    df = df.iloc[0:10]
    df.plot(kind='bar')
    savefig(f"{current_path}/../../.pytest_cache/test_rank.png")