from fastapi import APIRouter, Depends, status
from sqlalchemy import select, insert, delete, update

from database import get_async_session
from .models import Department
from .schemas import DepartmentCreateSchema, DepartmentReadSchema, DepartmentUpdateSchema

router = APIRouter(tags=["departments"], prefix="/departments")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание отделения
async def create_department(department: DepartmentCreateSchema,
                            session=Depends(get_async_session)) -> DepartmentReadSchema:
    statement = insert(Department).values(
        profile=department.profile,
        director=department.director,
        number_beds=department.number_beds,
        staff=department.staff,
        corpus=department.corpus
    ).returning(Department)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получает данные о всех отделениях
async def get_department(session=Depends(get_async_session)) -> list[DepartmentReadSchema]:
    statement = select(Department)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{department_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получает данные об отделении по id
async def get_department_by_id(department_id: int, session=Depends(get_async_session)) -> DepartmentReadSchema:
    statement = select(Department).where(Department.id == department_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{department_id", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление отделения по id
async def delete_department_by_id(department_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Department).where(Department.id == department_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{department_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных
async def update_department_by_id(department_id: int, department: DepartmentUpdateSchema,
                                  session=Depends(get_async_session)) -> DepartmentReadSchema:
    statement = update(Department).where(Department.id == department_id).values(
        profile=department.profile,
        director=department.director,
        number_beds=department.number_beds,
        staff=department.staff,
        corpus=department.corpus
    ).returning(Department)
    result = await session.scalar(statement)
    await session.commit()
    return result


