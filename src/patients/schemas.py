from datetime import datetime

from pydantic import BaseModel


class PatientReadSchema(BaseModel):
    id: int
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента
    created_at: datetime
    updated_at: datetime


class PatientCreateSchema(BaseModel):
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента


class PatientUpdateSchema(BaseModel):
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента
