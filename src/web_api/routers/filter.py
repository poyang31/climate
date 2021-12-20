from typing import Union

from fastapi import APIRouter
from pymongo import DESCENDING

from . import articles_collection
from ...crawler.models import Article

router = APIRouter()


@router.get("/")
def read_filter(keyword: str = "", page: int = 1) -> Union[list, None]:
    if page < 0 or not keyword:
        return None
    offset = (page - 1) * 10
    limit = page * 10
    result = articles_collection \
        .find({"words": {"$in": [keyword]}}) \
        .sort("updated_time", DESCENDING) \
        .skip(offset) \
        .limit(limit)
    return [Article.parse_obj(i) for i in result]
