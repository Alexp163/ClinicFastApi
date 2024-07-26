from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Personnel(Base):  # модель персонала
    __tablename__ = "personnel"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()  # ФИО
    age: Mapped[str] = mapped_column()  # возраст
    education: Mapped[str] = mapped_column()  # образование
    experience: Mapped[str] = mapped_column()  # опыт работы
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления
