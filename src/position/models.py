from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Position(Base):  # модель должности
    __tablename__ = "position"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()  # название должности
    duty: Mapped[str] = mapped_column()  # должностные обязанности
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления
