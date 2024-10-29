from datetime import datetime

from pydantic import BaseModel


class BuildingReadSchema(BaseModel):
    id: int
    clinic_id: int | None
    name: str
    profile: str
    year_release: str
    floors: str
    created_at: datetime
    updated_at: datetime


class BuildingCreateSchema(BaseModel):
    clinic_id: str | None
    name: str
    profile: str
    year_release: str
    floors: str


class BuildingUpdateSchema(BaseModel):
    clinic_id: str | None
    name: str
    profile: str
    year_release: str
    floors: str
