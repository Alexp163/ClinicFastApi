from fastapi import APIRouter, Depends, status
from sqlalchemy import insert, select, delete, update

from database import get_async_session
from .models import HospitalRoom
from .schemas import HospitalRoomCreateSchema, HospitalRoomReadSchema, HospitalRoomUpdateSchema

router = APIRouter(tags=["hospital_room"], prefix="/hospital_room")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание палаты
async def create_hospital_room(hospital_room: HospitalRoomCreateSchema, session=Depends(get_async_session)) -> HospitalRoomCreateSchema:
    statement = insert(HospitalRoom).values(
        number=hospital_room.number,
        number_beds=hospital_room.number_beds,
        nurse=hospital_room.nurse,
    ).returning(HospitalRoom)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) Получает данные о всех палатах
async def get_hospital_room(session=Depends(get_async_session)) -> list[HospitalRoomReadSchema]:
    statement = select(HospitalRoom)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{hospital_room_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получает данные о палате по id
async def get_hospital_room_by_id(hospital_room_id: int, session=Depends(get_async_session)) -> HospitalRoomReadSchema:
    statement = select(HospitalRoom).where(HospitalRoom.id == hospital_room_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{hospital_room_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) Удаление палаты по id
async def delete_hospital_room_by_id(hospital_room_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(HospitalRoom).where(HospitalRoom.id == hospital_room_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{hospital_room_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных
async def update_hospital_room_by_id(hospital_room_id: int, hospital_room: HospitalRoomUpdateSchema,
                                     session=Depends(get_async_session)) -> HospitalRoomUpdateSchema:
    statement = update(HospitalRoom).where(HospitalRoom.id == hospital_room_id).values(
        number=hospital_room.number,
        number_beds=hospital_room.number_beds,
        nurse=hospital_room.nurse,
    ).returning(HospitalRoom)
    result = await session.scalar(statement)
    await session.commit()
    return result


