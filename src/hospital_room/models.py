# from database import Base
# from sqlalchemy.orm import Mapped, mapped_column
# from datetime import datetime
# from sqlalchemy.sql import func
#
#
# class HospitalRoom(Base):  # модель палаты
#     __tablename__ = "hospital_room"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     number: Mapped[str] = mapped_column()  # номер палаты
#     number_beds: Mapped[str] = mapped_column()  # количество коек
#     doctor: Mapped[str] = mapped_column()  # лечащий врач
#     nurse: Mapped[str] = mapped_column()  # палатная медсестра
#     department: Mapped[str] = mapped_column()  # палата из отделения
#     created_at: Mapped[datetime] = mapped_column(server_default=func.now())
#     updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
