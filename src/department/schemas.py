from datetime import datetime

from pydantic import BaseModel


class DepartmentReadSchema(BaseModel):  # считать данные об отделении
    id: int
    profile: str  # профиль отделения
    director: str  # руководитель отделения
    number_beds: str  # количество коек
    staff: str  # штат сотрудников
    corpus: str  # в каком корпусе находится отделение
    created_at: datetime
    updated_at: datetime


class DepartmentCreateSchema(BaseModel):  # создать отделение
    profile: str  # профиль отделения
    director: str  # руководитель отделения
    number_beds: str  # количество коек
    staff: str  # штат сотрудников
    corpus: str  # в каком корпусе находится отделение


class DepartmentUpdateSchema(BaseModel):  # обновление данных
    profile: str  # профиль отделения
    director: str  # руководитель отделения
    number_beds: str  # количество коек
    staff: str  # штат сотрудников
    corpus: str  # в каком корпусе находится отделение
