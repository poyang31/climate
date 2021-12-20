from typing import Union

from fastapi import APIRouter
from pymongo import DESCENDING

from . import articles_collection
from ...crawler import Crawler
from ...crawler.models import Article
from ...crawler.ptt import PTT

router = APIRouter()


@router.get("/")
def read_filter(keyword: str = "") -> Union[dict, None]:
    count = articles_collection \
        .count_documents({"words": {"$in": [keyword]}})
    origin_count = {
        i.name: articles_collection.count_documents({"origin": i.name, "words": {"$in": [keyword]}})
        for i in Crawler.crawlers
    }
    return {
        "count": count,
        "origin_count": origin_count
    }
