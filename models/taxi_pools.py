from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey
from core.config import Base, fake


class TaxiPoolsModel(Base):
    __tablename__ = "taxi_pools"
    id = Column(Integer, primary_key=True)
    region_id = Column(Integer, ForeignKey("regions.id"), nullable=False)
    name = Column(String(100), nullable=False, unique=True)

    @staticmethod
    def fake(i) -> TaxiPoolsModel:
        return TaxiPoolsModel(region_id=fake.random_int(1, 10), name=fake.company())
