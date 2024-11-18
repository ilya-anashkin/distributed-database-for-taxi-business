from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from core.config import Base, fake

class CarRentsModel(Base):
    __tablename__ = 'car_rents'
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=False)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    finish_date = Column(Date)

    @staticmethod
    def fake() -> CarRentsModel:
        return CarRentsModel(
            driver_id=fake.random_int(1, 10),
            car_id=fake.random_int(1, 10),
            start_date=fake.date(),
            finish_date=fake.date()
        )
