from fastapi import APIRouter
from . import results_collection
from ...analysis.models import Result
from pandas import Series, read_json
from typing import Union, Mapping

router = APIRouter()


@router.get("/")
def read_rank() -> Union[Mapping, None]:
    data = results_collection.find_one({"name": "common"})
    if data is None:
        return None
    result = Result.parse_obj(data)
    df = read_json(result.content)
    se = Series(index=df[0].values, data=df[1].values)
    return se.to_dict()
