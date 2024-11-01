from fastapi import APIRouter, status, Depends
from sqlalchemy import select, insert, delete, update

from database import get_async_session
from .models import Position
from .schemas import PositionCreateSchema, PositionReadSchema, PositionUpdateSchema

router = APIRouter(tags=["positions"], prefix="/positions")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание должности
async def created_position(position: PositionCreateSchema, session=Depends(get_async_session)) -> PositionReadSchema:
    statement = insert(Position).values(  # statement-заявление
        title=position.title,
        duty=position.duty
    ).returning(Position)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) получает данные о всех должностях
async def get_position(session=Depends(get_async_session)) -> list[PositionReadSchema]:
    statement = select(Position)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{position_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получение данных о должности по id
async def get_position_by_id(position_id: int, session=Depends(get_async_session)) -> PositionReadSchema:
    statement = select(Position).where(Position.id == position_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{position_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4)  удаление данных должности по id
async def delete_position_by_id(position_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Position).where(Position.id == position_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{position_id}", status_code=status.HTTP_200_OK)  # 5) обновление данных должности по id
async def update_session_by_id(position_id: int, position: PositionUpdateSchema,
                               session=Depends(get_async_session)) -> PositionReadSchema:
    statement = update(Position).where(Position.id == position_id).values(
        title=position.title,
        duty=position.duty
    ).returning(Position)
    result = await session.scalar(statement)
    await session.commit()
    return result

