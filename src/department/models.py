from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base


class Department(Base):  # модель отделения
    __tablename__ = "department"
    id: Mapped[int] = mapped_column(primary_key=True)
    building_id: Mapped[int | None] = mapped_column(ForeignKey("building.id"))
    building = relationship("Building")
    profile: Mapped[str] = mapped_column()  # профиль отделения
    director: Mapped[str] = mapped_column()  # руководитель отделения
    number_beds: Mapped[str] = mapped_column()  # количество коек
    staff: Mapped[str] = mapped_column()  # штат сотрудников
    corpus: Mapped[str] = mapped_column()  # в каком корпусе находится отделение
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.director} {self.number_beds} {self.corpus}"
