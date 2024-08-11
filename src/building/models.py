from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from database import Base


class Building(Base):
    __tablename__ = "building"
    id: Mapped[int] = mapped_column(primary_key=True)
    # clinic_id: Mapped[int] = mapped_column(ForeignKey("clinics.id"))
    name: Mapped[str] = mapped_column()
    profile: Mapped[str] = mapped_column()
    year_release: Mapped[str] = mapped_column()
    floors: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
