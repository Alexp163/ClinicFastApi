from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.sql import func


class Doctor(Base):
    __tablename__ = "doctors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # ФИО
    special: Mapped[str] = mapped_column()  # специальность
    experience: Mapped[str] = mapped_column()  # стаж работы
    working_hours: Mapped[str] = mapped_column()  # часы работы
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
