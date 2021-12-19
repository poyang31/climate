from typing import Optional

from pydantic import BaseModel


class Article(BaseModel):
    origin: str
    class_: str
    tag: str
    title: str
    content: str
    url: str
    words: list
    created_time: int
    updated_time: int
    captured_time: Optional[int]
