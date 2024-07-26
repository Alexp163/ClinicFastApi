from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.asyncio import AsyncEngine
from .dependecies import Clinic, Building, User, Doctor, Department, Patient, HospitalRoom, Personnel


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


class DepartmentModelView(ModelView, model=Department):
    column_list = [Department.profile, Department.director, Department.number_beds, Department.staff, Department.corpus]
    form_excluded_columns = [Department.created_at, Department.updated_at]


class PatientModelView(ModelView, model=Patient):
    column_list = [Patient.name, Patient.age, Patient.address, Patient.diagnosis]
    form_excluded_columns = [Patient.created_at, Patient.updated_at]


class HospitalRoomModelView(ModelView, model=HospitalRoom):
    column_list = [HospitalRoom.number, HospitalRoom.number_beds, HospitalRoom.nurse]
    form_excluded_columns = [HospitalRoom.created_at, HospitalRoom.updated_at]


class PersonnelModelView(ModelView, model=Personnel):
    column_list = [Personnel.name, Personnel.age, Personnel.education, Personnel.experience]
    form_excluded_columns = [Personnel.created_at, Personnel.updated_at]


def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(ClinicModelView)
    admin.add_view(BuildingModelView)
    admin.add_view(UserModelView)
    admin.add_view(DoctorModelView)
    admin.add_view(DepartmentModelView)
    admin.add_view(PatientModelView)
    admin.add_view(HospitalRoomModelView)
    admin.add_view(PersonnelModelView)

