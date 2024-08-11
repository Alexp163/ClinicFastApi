from datetime import datetime

from pydantic import BaseModel


class DoctorReadSchema(BaseModel):
    id: int
    name: str  # имя доктора
    special: str  # специальность
    experience: str  # стаж работы
    working_hours: str  # часы работы
    created_at: datetime
    updated_at: datetime


class DoctorCreateSchema(BaseModel):
    name: str
    special: str
    experience: str
    working_hours: str


class DoctorUpdateSchema(BaseModel):
    name: str
    special: str
    experience: str
    working_hours: str
