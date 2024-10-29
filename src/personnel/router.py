from fastapi import APIRouter, status, Depends
from .models import Personnel
from database import get_async_session
from sqlalchemy import select, insert, delete, update
from .schemas import PersonnelCreateSchema, PersonnelUpdateSchema, PersonnelReadSchema

router = APIRouter(tags=["personnels"], prefix="/personnels")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание персонала
async def create_personnel(personnel: PersonnelCreateSchema,
                           session=Depends(get_async_session)) -> PersonnelReadSchema:
    statement = insert(Personnel).values(
    name=personnel.name,  # Ф.И.О
    age=personnel.age,  # возраст
    education=personnel.education,  # образование
    experience=personnel.experience  # опыт работы
    ).returning(Personnel)
    result = await session.scalar(statement)
    await session.commit
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) получает данные о всем персонале
async def get_personnel(session=Depends(get_async_session)) -> list[PersonnelReadSchema]:
    statement = select(Personnel)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{personnel_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получает данные о персонале по id
async def get_personnel_by_id(personnel_id: int, session=Depends(get_async_session)) -> PersonnelReadSchema:
    statement = select(Personnel).where(Personnel.id == personnel_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{personnel_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаление персонала по id
async def delete_personnel_by_id(personnel_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Personnel).where(Personnel.id == personnel_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{personnel_id}", status_code=status.HTTP_200_OK)  # 5) обновление данных по персоналу
async def update_personnel_by_id(personnel_id: int, personnel: PersonnelUpdateSchema,
                                 session=Depends(get_async_session)) -> PersonnelReadSchema:
    statement = update(Personnel).where(Personnel.id == personnel_id).values(
        name=personnel.name,  # Ф.И.О
        age=personnel.age,  # возраст
        education=personnel.education,  # образование
        experience=personnel.experience  # опыт работы
    ).returning(Personnel)
    result = await session.scalar(statement)
    await session.commit()
    return result




