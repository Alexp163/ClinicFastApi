from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.asyncio import AsyncEngine
from .dependecies import Clinic, Building, User, Doctor


class ClinicModelView(ModelView, model=Clinic):
    column_list = [Clinic.name, Clinic.address]
    form_excluded_columns = [Clinic.created_at, Clinic.updated_at]


class BuildingModelView(ModelView, model=Building):
    column_list = [Building.name, Building.profile, Building.year_release,
                   Building.floors]
    form_excluded_columns = [Building.created_at, Building.updated_at]


class UserModelView(ModelView, model=User):
    column_list = [User.name, User.age, User.email, User.address, User.password]
    form_excluded_columns = [User.created_at, User.updated_at]


class DoctorModelView(ModelView, model=Doctor):
    column_list = [Doctor.name, Doctor.special, Doctor.experience, Doctor.working_hours]
    form_excluded_columns = [Doctor.created_at, Doctor.updated_at]


def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(ClinicModelView)
    admin.add_view(BuildingModelView)
    admin.add_view(UserModelView)
    admin.add_view(DoctorModelView)
