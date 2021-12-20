from typing import Union, Mapping

from fastapi import APIRouter
from pandas import Series, read_json
from pymongo import DESCENDING

from . import results_collection
from ...analysis.models import Result

router = APIRouter()


@router.get("/")
def read_rank() -> Union[Mapping, None]:
    data = results_collection.find({"name": "common"}).sort("captured_time", DESCENDING).limit(1)
    if data is None:
        return None
    result = Result.parse_obj(data.next())
    df = read_json(result.content)
    se = Series(index=df[0].values, data=df[1].values)
    return se.to_dict()
