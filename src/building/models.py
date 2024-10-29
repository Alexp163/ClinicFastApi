from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base


class Building(Base):
    __tablename__ = "building"
    id: Mapped[int] = mapped_column(primary_key=True)
    clinic_id: Mapped[int | None] = mapped_column(ForeignKey("clinic.id"))
    clinic = relationship("Clinic")
    name: Mapped[str] = mapped_column()  # Название корпуса
    profile: Mapped[str] = mapped_column()  # профиль работы
    year_release: Mapped[str] = mapped_column()  # год постройки
    floors: Mapped[str] = mapped_column()  # количество этажей
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.name} {self.profile} {self.year_release} {self.floors}"
