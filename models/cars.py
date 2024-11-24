from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from core.config import Base, fake

class CarsModel(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    taxi_pool_id = Column(Integer, ForeignKey('taxi_pools.id'), nullable=False)
    car_model_rbi_id = Column(Integer, ForeignKey('car_models.id'), nullable=False)
    last_inspection_date = Column(Date)
    register_date = Column(Date, nullable=False)
    unregister_date = Column(Date)
    vin_number = Column(String(17), nullable=False, unique=True)

    @staticmethod
    def fake() -> CarsModel:
        return CarsModel(
            taxi_pool_id=fake.random_int(1, 10),
            car_model_rbi_id=fake.random_int(1, 10),
            last_inspection_date=fake.date(),
            register_date=fake.date(),
            unregister_date=fake.date(),
            vin_number=fake.vin()
        )
