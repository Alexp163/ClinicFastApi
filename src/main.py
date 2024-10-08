from fastapi import FastAPI

from admin.panel import register_admin
from building.router import router as building_router
from clinic.router import router as clinic_router
from database import engine
from department.router import router as department_router
from doctors.router import router as doctor_router
from hospital_room.router import router as hospital_room_router
from patients.router import router as patient_router
from personnel.router import router as personnel_router
from position.router import router as position_router
from users.router import router as users_router

app = FastAPI()
app.include_router(building_router)
app.include_router(users_router)
app.include_router(clinic_router)
app.include_router(doctor_router)
app.include_router(department_router)
app.include_router(patient_router)
app.include_router(hospital_room_router)
app.include_router(personnel_router)
app.include_router(position_router)

register_admin(app, engine)

