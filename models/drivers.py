from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger
from core.config import Base, fake

class DriversModel(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    taxi_pool_id = Column(Integer, ForeignKey('taxi_pools.id'), nullable=False)
    employment_status_id = Column(Integer, ForeignKey('employment_statuses.id'), nullable=False)
    name = Column(String(100), nullable=False)
    phone = Column(String(30), nullable=False)
    passport = Column(String(10), nullable=False, unique=True)
    license = Column(String(10), nullable=False, unique=True)
    register_date = Column(Date, nullable=False)
    unregister_date = Column(Date)
    rating = Column(SmallInteger, nullable=False)

    @staticmethod
    def fake() -> DriversModel:
        return DriversModel(
            taxi_pool_id=fake.random_int(1, 10),
            employment_status_id=fake.random_int(1, 10),
            name=' '.join([fake.first_name(), fake.last_name()]),
            phone=fake.phone_number(),
            passport=str(fake.random_int(1000000000, 9999999999)),
            license=str(fake.random_int(1000000000, 9999999999)),
            register_date=fake.date(),
            unregister_date=fake.date(),
            rating=fake.random_int(1, 100)
        )
