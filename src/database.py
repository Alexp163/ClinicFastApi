from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/clinic_api"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(engine)
Base = declarative_base()
