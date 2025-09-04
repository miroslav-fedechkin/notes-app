from typing import Optional
from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    id: int


class STaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class STaskDelete(BaseModel):
    id: int