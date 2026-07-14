from pydantic import BaseModel
from typing import Any
from datetime import datetime


class BaseResponse(BaseModel):
    statusCode: int
    message: str
    error: str | None = None
    data: Any = None
    path: str
    timestamp: datetime