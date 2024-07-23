from fastapi import APIRouter, Depends, status
from .models import Doctor
from database import get_async_session
from sqlalchemy import select, insert, delete, update

from .schemas import DoctorCreateSchema, DoctorReadSchema, DoctorUpdateSchema

router = APIRouter(tags=["doctors"], prefix="/doctors")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание доктора
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


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получает данные о всех докторах
async def get_doctors(session=Depends(get_async_session)) -> list[DoctorReadSchema]:
    statement = select(Doctor)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{doctor_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получение данных о докторе по id
async def get_doctor_by_id(doctor_id: int, session=Depends(get_async_session)) -> DoctorReadSchema:
    statement = select(Doctor).where(Doctor.id == doctor_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление доктора по id
async def delete_doctor_by_id(doctor_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Doctor).where(Doctor.id == doctor_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{doctor_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных
async def update_doctor_by_id(doctor_id: int, doctor: DoctorUpdateSchema, session=Depends(get_async_session)) -> DoctorUpdateSchema:
    statement = update(Doctor).where(Doctor.id == doctor_id).values(
        name=doctor.name,
        special=doctor.special,
        experience=doctor.experience,
        working_hours=doctor.working_hours
    ).returning(Doctor)
    result = await session.scalar(statement)
    await session.commit()
    return result
