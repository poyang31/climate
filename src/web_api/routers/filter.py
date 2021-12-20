from fastapi import APIRouter
from ...kernel import Config, Database

router = APIRouter()

config = Config()
database = Database(config)


@router.get("/hi")
def read_filter():
    return {"Hi": 1234}
