from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Clinic(Base):  # модель клиники
    __tablename__ = "clinic"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())  # дата создания
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())  # дата обновления

    def __repr__(self):
        return f"{self.id} {self.name} {self.address}"
