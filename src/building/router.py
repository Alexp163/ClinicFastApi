from fastapi import APIRouter, Depends

from .models import Clinic
from database import get_async_session
from sqlalchemy import select, insert, delete, update

from .schemas import ClinicReadSchema

router = APIRouter()


@router.get("/clinics")
async def get_clinics(session = Depends(get_async_session)) ->list[ClinicReadSchema]:
    statement = select(Clinic)
    result = await session.scalars(statement)
    return result


@router.get("/clinics/{clinic_id}")
async def get_clinic_by_id(clinic_id: int, session = Depends(get_async_session)) ->ClinicReadSchema:
    statement = select(Clinic).where(Clinic.id == clinic_id)
    result = await session.scalar(statement)
    return result


@router.delete("/clinics/{clinic_id}")
async def delete_clinic_by_id(clinic_id: int, session = Depends(get_async_session)):
    statement = delete(Clinic).where(Clinic.id == clinic_id)
    await session.execute(statement)
    await session.commit()
    return "ok"



