from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Doctor(Base):
    __tablename__ = "doctor"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # ФИО
    special: Mapped[str] = mapped_column()  # специальность
    experience: Mapped[str] = mapped_column()  # стаж работы
    working_hours: Mapped[str] = mapped_column()  # часы работы
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.name} {self.special}"
