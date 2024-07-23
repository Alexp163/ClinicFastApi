from fastapi import APIRouter, Depends, status

from .models import Building
from database import get_async_session
from sqlalchemy import select, insert, delete, update

from .schemas import BuildingCreateSchema, BuildingReadSchema, \
    BuildingUpdateSchema

router = APIRouter(tags=["buildings"], prefix="/buildings")


@router.post("/", status_code=status.HTTP_201_CREATED)  # 1) создание отдельной постройки(здания)
async def create_building(building: BuildingCreateSchema, session=Depends(get_async_session)) -> BuildingCreateSchema:
    statement = insert(Building).values(
        name=building.name,
        profile=building.profile,
        year_release=building.year_release,
        floors=building.floors
    ).returning(Building)
    result = await session.scalar(statement)
    await session.commit()
    return result


@router.get("/", status_code=status.HTTP_202_ACCEPTED)  # 2) получение данных о всех постройках(зданиях клиники)
async def get_buildings(session=Depends(get_async_session)) ->list[BuildingReadSchema]:
    statement = select(Building)
    result = await session.scalars(statement)
    return list(result)


@router.get("/{building_id}", status_code=status.HTTP_202_ACCEPTED)  # 3) получение данных о здании клиники по id
async def get_building_by_id(building_id: int, session=Depends(get_async_session)) -> BuildingReadSchema:
    statement = select(Building).where(Building.id == building_id)
    result = await session.scalar(statement)
    return result


@router.delete("/{building_id}", status_code=status.HTTP_204_NO_CONTENT)  # 4) удаление здания клиники по id
async def delete_building_by_id(building_id: int, session=Depends(get_async_session)) -> None:
    statement = delete(Building).where(Building.id == building_id)
    await session.execute(statement)
    await session.commit()


@router.put("/{building_id}", status_code=status.HTTP_200_OK)  # 5) Обновление данных
async def update_building_by_id(building_id: int, building: BuildingUpdateSchema, session=Depends(get_async_session)) -> BuildingUpdateSchema:
    statement = update(Building).where(Building.id == building_id).values(
        name=building.name,
        profile=building.profile,
        year_release=building.year_release,
        floors=building.floors
    ).returning(Building)
    result = await session.scalar(statement)
    await session.commit()
    return result



