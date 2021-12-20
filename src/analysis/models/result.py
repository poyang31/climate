from typing import Any, Optional

from pydantic import BaseModel


class Result(BaseModel):
    name: str
    content: Any
    captured_time: Optional[int]
