from fastapi import APIRouter, Depends, status
from .models import Patient
from database import get_async_session
from sqlalchemy import select, insert, delete, update

from .schemas import PatientCreateSchema, PatientReadSchema, PatientUpdateSchema

router = APIRouter(tags=["patients"], prefix="/patients")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание пациента
async def create_patient(patient: PatientCreateSchema, session=Depends(get_async_session)) -> PatientReadSchema:
    statement = insert(Patient).values(
        name=patient.name,  # ФИО пациента
        age=patient.age,  # возраст пациента
        address=patient.address, # адрес пациента
        diagnosis=patient.diagnosis # диагноз пациента
    ).returning(Patient)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получает данные о всех пациентах
async def get_patients(session=Depends(get_async_session)) -> list[PatientReadSchema]:
    statement = select(Patient)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{patient_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получение данных о пациенте по id
async def get_patient_by_id(patient_id: int, session=Depends(get_async_session)) -> PatientReadSchema:
    statement = select(Patient).where(Patient.id == patient_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление пациента по id
async def delete_patient_by_id(patient_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Patient).where(Patient.id == patient_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{patient_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных
async def update_patient_by_id(patient_id: int, patient: PatientUpdateSchema,
                               session=Depends(get_async_session)) -> PatientReadSchema:
    statement = update(Patient).where(Patient.id == patient_id).values(
        name=patient.name,  # ФИО пациента
        age=patient.age,  # возраст пациента
        address=patient.address,  # адрес пациента
        diagnosis=patient.diagnosis  # диагноз пациента
    ).returning(Patient)
    result = await session.scalar(statement)
    await session.commit()
    return result
