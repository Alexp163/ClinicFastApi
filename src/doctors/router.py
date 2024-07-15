from fastapi import APIRouter, Depends
from .models import Doctor
from database import get_async_session
from sqlalchemy import select, insert, delete, update

from .schemas import DoctorCreateSchema, DoctorReadSchema

router = APIRouter(tags=["doctors"], prefix="/doctors")


@router.post("/")  # 1) Создание доктора
async def create_doctor(doctor: DoctorCreateSchema, session=Depends(get_async_session)) -> DoctorCreateSchema:
    statement = insert(Doctor).values(
        name=doctor.name,
        cpecial=doctor.special,
        experience=doctor.experience,
        working_hours=doctor.working_hours
    ).returning(Doctor)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/")  # 2) Получает данные о всех докторах
async def get_doctors(session=Depends(get_async_session)) -> list[DoctorReadSchema]:
    statement = select(Doctor)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{doctor_id}")  # 3) получение данных о докторе по id
async def get_doctor_by_id(doctor_id: int, session=Depends(get_async_session)) -> DoctorReadSchema:
    statement = select(Doctor).where(Doctor.id == doctor_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{doctor_id}")  # 4) Удаление доктора по id
async def delete_doctor_by_id(doctor_id: int, session=Depends(get_async_session)):
    statement = delete(Doctor).where(Doctor.id == doctor_id)
    await session.execute(statement)
    await session.commit()
    return "ok"







