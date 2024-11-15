from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger
from config import Base, fake

class DriversStatusesModel(Base):
    __tablename__ = 'drivers_statuses'
    id = Column(Integer, primary_key=True)
    status = Column(String(50), nullable=False, unique=True)

    @staticmethod
    def fake() -> DriversStatusesModel:
        return DriversStatusesModel(
            status=fake.word()
        )
