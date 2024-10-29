from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database import Base


class Patient(Base):
    __tablename__ = "patient"
    id: Mapped[int] = mapped_column(primary_key=True)
    doctor_id: Mapped[int | None] = mapped_column(ForeignKey("doctor.id"))
    doctor = relationship("Doctor")
    user_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship("User")
    hospital_room_id: Mapped[int | None] = mapped_column(ForeignKey("hospital_room.id"))
    hospital_room = relationship("HospitalRoom")
    name: Mapped[str] = mapped_column()  # ФИО
    age: Mapped[str] = mapped_column()  # возраст
    address: Mapped[str] = mapped_column()  # адрес
    diagnosis: Mapped[str] = mapped_column()  # диагноз
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.name} {self.age} {self.diagnosis}"


