from pydantic import BaseModel


class PersonnelReadSchema(BaseModel):
    id: int
    name: str  # Ф.И.О
    age: str  # возраст
    education: str  # образование
    experience: str  # опыт работы


class PersonnelCreateSchema(BaseModel):
    name: str  # Ф.И.О
    age: str  # возраст
    education: str  # образование
    experience: str  # опыт работы


class PersonnelUpdateSchema(BaseModel):
    name: str  # Ф.И.О
    age: str  # возраст
    education: str  # образование
    experience: str  # опыт работы

