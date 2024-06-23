from fastapi import APIRouter, Depends
from .models import Doctor
from database import get_async_session
from sqlalchemy import select, unsert, delete, update

from .schemas import DoctorCreateSchema, DoctorReadSchema

router = APIRouter()

