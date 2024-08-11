from datetime import datetime

from pydantic import BaseModel


class PositionReadSchema(BaseModel):
    id: int
    title: str
    duty: str
    created_at: datetime
    updated_at: datetime


class PositionCreateSchema(BaseModel):
    title: str
    duty: str


class PositionUpdateSchema(BaseModel):
    title: str
    duty: str
