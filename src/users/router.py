from fastapi import APIRouter, Depends

from .models import User
from database import get_async_session
from sqlalchemy import select, insert, delete, update
from .schemas import UserReadSchema, UserCreateSchema

router = APIRouter()


@router.post("/user")  # 1) Создание пользователя
async def create_user(user: UserCreateSchema, session=Depends(get_async_session)) -> UserReadSchema:
    statement = insert(User).values(
        name=user.name,
        age=user.age,
        email=user.email,
        address=user.address,
        password=user.password,
    ).returning(User)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/users")  # 2) получает данные о всех пользователях
async def get_users(session=Depends(get_async_session)) -> list[UserReadSchema]:
    statement = select(User)
    result = await session.scalars(statement)
    return list(result)


@router.get("/users/{user_id}")  # 3) Получение данных о пользователе по id
async def get_user_by_id(user_id: int, session=Depends(get_async_session)) -> UserReadSchema:
    statement = select(User).where(User.id == user_id)
    result = await session.scalar(statement)
    return result


@router.delete("/users/{user_id}")  # 4) Удаление данных о пользователе по id
async def delete_users_by_id(user_id: int, session=Depends(get_async_session)):
    statement = delete(User).where(User.id == user_id)
    await session.execute(statement)
    await session.commit()
    return "ok"
