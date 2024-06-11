from database import Base
from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.sql import func


class Clinic(Base):
    __tablename__ = "clinic"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    address = Column(String(255))
    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())  # дата обновления


class Corpus(Base):
    __tablename__ = "corpus"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    profile = Column(String(200))
    year_release = Column(String(100))
    floors = Column(String(100))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
