from fastapi import APIRouter, Depends, status
from sqlalchemy import select, insert, delete, update

from database import get_async_session
from .models import Clinic
from .schemas import ClinicReadSchema, ClinicCreateSchema, ClinicUpdateSchema

router = APIRouter(tags=["clinics"], prefix="/clinics")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание клиники
async def create_clinic(clinic: ClinicCreateSchema, session=Depends(get_async_session)) -> ClinicReadSchema:
    statement = insert(Clinic).values(  # "statement" - заявление
        name=clinic.name,
        address=clinic.address
    ).returning(Clinic)
    result = await session.scalar(statement)
    await session.commit()  # "await" -ожидать
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) получает данные о всех клиниках
async def get_clinics(session=Depends(get_async_session)) -> list[ClinicReadSchema]:  # "Depends" - зависит
    statement = select(Clinic)  # "statement" - заявление
    result = await session.scalars(statement)  # "await" -ожидать
    return list(result)


@router.get("/{clinic_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получение данных о клинике по id
async def get_clinic_by_id(clinic_id: int, session=Depends(get_async_session)) -> ClinicReadSchema:
    statement = select(Clinic).where(Clinic.id == clinic_id)  # "where" - где
    result = await session.scalar(statement)  # "await" -ожидать
    return result


@router.delete("/{clinic_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаление клиники по id
async def delete_clinic_by_id(clinic_id: int, session=Depends(get_async_session)) -> None:  # "Depends" - зависит
    statement = delete(Clinic).where(Clinic.id == clinic_id)  # "where" - где
    await session.execute(statement)  # "execute" - выполнять
    await session.commit()


@router.put("/{clinic_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных по клинике по id
async def update_clinic_by_id(clinic_id: int, clinic: ClinicUpdateSchema,
                              session=Depends(get_async_session)) -> ClinicReadSchema:
    statement = update(Clinic).where(Clinic.id == clinic_id).values(  # "where" - где
        name=clinic.name,
        address=clinic.address
    ).returning(Clinic)
    result = await session.scalar(statement)
    await session.commit()
    return result

