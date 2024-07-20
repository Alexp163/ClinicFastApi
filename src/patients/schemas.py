from pydantic import BaseModel


class PatientReadSchema(BaseModel):
    id: int
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента


class PatientCreateSchema(BaseModel):
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента


class PatientDeleteSchema(BaseModel):
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента


class PatientUpdateSchema(BaseModel):
    name: str  # ФИО пациента
    age: str  # возраст пациента
    address: str  # адрес пациента
    diagnosis: str  # диагноз пациента
