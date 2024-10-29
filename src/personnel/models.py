from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base


class Personnel(Base):  # модель персонала
    __tablename__ = "personnel"
    id: Mapped[int] = mapped_column(primary_key=True)
    positions: Mapped[list["Position"]] = relationship("Position", secondary="personnel2position")
    name: Mapped[str] = mapped_column()  # ФИО
    age: Mapped[str] = mapped_column()  # возраст
    education: Mapped[str] = mapped_column()  # образование
    experience: Mapped[str] = mapped_column()  # опыт работы
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return f"{self.name} {self.age} {self.education} {self.experience}"


class Personnel2Position(Base):  # связь между персоналом и позицией(многие ко многим)
    __tablename__ = "personnel2position"
    id: Mapped[int] = mapped_column(primary_key=True)
    personnel_id: Mapped[int | None] = mapped_column(ForeignKey("personnel.id"))
    position_id: Mapped[int | None] = mapped_column(ForeignKey("position.id"))

    def __repr__(self):
        return f"{self.personnel_id} {self.position_id}"
