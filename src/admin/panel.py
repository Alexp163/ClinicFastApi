from fastapi import FastAPI
from sqladmin import Admin, ModelView
from sqlalchemy.ext.asyncio import AsyncEngine
from .dependecies import Clinic, Corpus



class ClinicModelView(ModelView, model=Clinic):
    column_list = [Clinic.name, Clinic.address]
    form_excluded_columns = [Clinic.created_at, Clinic.updated_at]


class CorpusModelView(ModelView, model=Corpus):
    column_list = [Corpus.name, Corpus.profile, Corpus.year_release, Corpus.floors]
    form_excluded_columns = [Corpus.created_at, Corpus.updated_at]


def register_admin(app: FastAPI, engine: AsyncEngine):
    admin = Admin(app, engine)
    admin.add_view(ClinicModelView)
    admin.add_view(CorpusModelView)





