from fastapi import APIRouter, Depends, status

from .models import User
from database import get_async_session
from sqlalchemy import select, insert, delete, update
from .schemas import UserReadSchema, UserCreateSchema, UserUpdateSchema

router = APIRouter(tags=["users"], prefix="/users")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) Создание пользователя
async def create_user(user: UserCreateSchema, session=Depends(get_async_session)) -> UserReadSchema:
    statement = insert(User).values(
        name=user.name,
        age=user.age,
        email=user.email,
        address=user.address,
        password=user.password
    ).returning(User)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) получает данные о всех пользователях
async def get_users(session=Depends(get_async_session)) -> list[UserReadSchema]:
    statement = select(User)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{user_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) Получение данных о пользователе по id
async def get_user_by_id(user_id: int, session=Depends(get_async_session)) -> UserReadSchema:
    statement = select(User).where(User.id == user_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление данных о пользователе по id
async def delete_users_by_id(user_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(User).where(User.id == user_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{user_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных
async def update_user_by_id(user_id: int, user: UserUpdateSchema, session=Depends(get_async_session)) -> UserReadSchema:
    statement = update(User).where(User.id == user_id).values(
        name=user.name,
        age=user.age,
        email=user.email,
        address=user.address,
        password=user.password
    ).returning(User)
    result = await session.scalar(statement)
    await session.commit()
    return result
