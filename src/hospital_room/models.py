from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class HospitalRoom(Base):  # модель палаты
    __tablename__ = "hospital_room"
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column()  # номер палаты
    number_beds: Mapped[str] = mapped_column()  # количество коек
    nurse: Mapped[str] = mapped_column()  # палатная медсестра
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"{self.id} {self.number} {self.number_beds} {self.nurse}"
