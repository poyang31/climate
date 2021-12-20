from typing import Optional

from pydantic import BaseModel


class Result(BaseModel):
    name: str
    content: str
    captured_time: Optional[int]
