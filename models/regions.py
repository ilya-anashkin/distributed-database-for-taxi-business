from __future__ import annotations

from sqlalchemy import Column, Integer, String, Float
from core.config import Base, fake

class RegionsModel(Base):
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    name = Column(String(100), nullable=False, unique=True)

    @staticmethod
    def fake() -> RegionsModel:
        return RegionsModel(
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            name=fake.city()
        )
