from database import Base
from sqlalchemy import Integer, Column, String


class Clinic(Base):
    __tablename__ = "clinic"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    address = Column(String(255))


class Corpus(Base):
    __tablename__ = "corpus"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    