from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy.sql import func


class Department(Base):  # модель отделения
    __tablename__ = "department"
    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped[str] = mapped_column()  # профиль отделения
    director: Mapped[str] = mapped_column()  # руководитель отделения
    number_beds: Mapped[str] = mapped_column()  # количество коек
    staff: Mapped[str] = mapped_column()  # штат сотрудников
    corpus: Mapped[str] = mapped_column()  # в каком корпусе находится отделение
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
