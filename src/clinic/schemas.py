from datetime import datetime

from pydantic import BaseModel


class ClinicReadSchema(BaseModel):
    id: int
    name: str
    address: str
    # created_at: datetime
    # updated_at: datetime


class ClinicCreateSchema(BaseModel):
    name: str
    address: str


class ClinicUpdateSchema(BaseModel):
    name: str
    address: str
