from datetime import datetime

from pydantic import BaseModel


class HospitalRoomReadSchema(BaseModel):  # считать данные о палате
    id: int
    number: str  # номер палаты
    number_beds: str  # количество коек
    nurse: str  # палатная медсестра
    created_at: datetime
    updated_at: datetime


class HospitalRoomCreateSchema(BaseModel):  # создать данные о палате
    number: str  # номер палаты
    number_beds: str  # количество коек
    nurse: str  # палатная медсестра


class HospitalRoomUpdateSchema(BaseModel):  # обновить данные о палате
    number: str  # номер палаты
    number_beds: str  # количество коек
    nurse: str  # палатная медсестра
