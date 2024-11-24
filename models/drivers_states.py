from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, Float
from core.config import Base, fake


class DriversStatesModel(Base):
    __tablename__ = "drivers_states"
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("drivers_statuses.id"), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    last_update_date = Column(Date, nullable=False)

    @staticmethod
    def fake(i) -> DriversStatesModel:
        return DriversStatesModel(
            driver_id=fake.random_int(1, 10),
            status_id=fake.random_int(1, 10),
            latitude=fake.latitude(),
            longitude=fake.longitude(),
            last_update_date=fake.date(),
        )
