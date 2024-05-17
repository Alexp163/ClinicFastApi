from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.asyncio import AsyncEngine
from .dependecies import Clinic


class ClinicModelView(ModelView, model=Clinic):
    pass


def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)


