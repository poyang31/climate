from typing import Optional

from pydantic import BaseModel


class Result(BaseModel):
    origin: str
    content: dict
    captured_time: Optional[int]
