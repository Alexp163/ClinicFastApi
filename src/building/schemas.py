from datetime import datetime

from pydantic import BaseModel


class BuildingCreateSchema(BaseModel):
    name: str
    profile: str
    year_release: str
    floors: str


class BuildingReadSchema(BaseModel):
    id: int
    name: str
    profile: str
    year_release: str
    floors: str
    created_at: datetime
    updated_at: datetime


class BuildingUpdateSchema(BaseModel):
    name: str
    profile: str
    year_release: str
    floors: str
