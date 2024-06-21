from fastapi import FastAPI
from admin.panel import register_admin
from database import engine
from building.router import router as building_router
from users.router import router as users_router
from clinic.router import router as clinic_router

app = FastAPI()
app.include_router(building_router)
app.include_router(users_router)
app.include_router(clinic_router)

register_admin(app, engine)

