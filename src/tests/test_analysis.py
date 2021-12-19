import pandas as pd
from collections import Counter
from ..kernel import Config, Database
from ..crawler.models import Article

temp=[]
def test_example():
    config = Config()
    database = Database(config)
    articles_collection = database.get_collection("articles")
    articles = [Article.parse_obj(i) for i in articles_collection.find({})]
    
    for i in articles:
        for s in i.words:
            temp.append(s)
    count=Counter(temp)
    common=count.most_common()
    df=pd.DataFrame(common)
    df=df.iloc[0:30]
    print(df)

    
