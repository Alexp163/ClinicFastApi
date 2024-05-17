from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from typing import AsyncGenerator


SQLALCHEMY_DATABASE_URI = "postgresql+asyncpg://postgres:1234@localhost:5432/clinic_api"
engine = create_async_engine(SQLALCHEMY_DATABASE_URI)
async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)
Base = declarative_base()
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

