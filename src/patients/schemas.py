from datetime import datetime

from pydantic import BaseModel


class PatientReadSchema(BaseModel):
    id: int
    doctor_id: str | None
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента
    created_at: datetime
    updated_at: datetime


class PatientCreateSchema(BaseModel):
    doctor_id: str | None
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента


class PatientUpdateSchema(BaseModel):
    doctor_id: str | None
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента
