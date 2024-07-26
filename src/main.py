from fastapi import FastAPI
from admin.panel import register_admin
from database import engine
from building.router import router as building_router
from users.router import router as users_router
from clinic.router import router as clinic_router
from doctors.router import router as doctor_router
from department.router import router as department_router
from patients.router import router as patient_router
from hospital_room.router import router as hospital_room_router
from personnel.router import router as personnel_router


app = FastAPI()
app.include_router(building_router)
app.include_router(users_router)
app.include_router(clinic_router)
app.include_router(doctor_router)
app.include_router(department_router)
app.include_router(patient_router)
app.include_router(hospital_room_router)
app.include_router(personnel_router)

register_admin(app, engine)

