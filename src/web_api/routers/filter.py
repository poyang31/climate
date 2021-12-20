from fastapi import APIRouter
from typing import Union
from . import articles_collection
from ...crawler.models import Article

router = APIRouter()


@router.get("/")
def read_filter(keyword: str = "") -> Union[list, None]:
    if not keyword:
        return None
    result = articles_collection.find({"words": {"$in": [keyword]}})
    return [Article.parse_obj(i) for i in result]
