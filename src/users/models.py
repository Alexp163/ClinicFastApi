from database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(String(10))
    email = Column(String(100))
    address = Column(String(255))
    password = Column(String(100))
