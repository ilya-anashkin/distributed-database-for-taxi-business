from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, Float
from config import Base, fake

class UnsatisfactoryRidesModel(Base):
    __tablename__ = 'unsatisfactory_rides'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    car_rent_id = Column(Integer, ForeignKey('car_rents.id'), nullable=False)
    client_feedback_stars = Column(SmallInteger)
    client_feedback_review = Column(String(500))
    driver_feedback_stars = Column(SmallInteger)

    @staticmethod
    def fake() -> UnsatisfactoryRidesModel:
        return UnsatisfactoryRidesModel(
            client_id=fake.random_int(1, 10),
            car_rent_id=fake.random_int(1, 10),
            client_feedback_stars=fake.random_int(1, 5),
            client_feedback_review=fake.text(),
            driver_feedback_stars=fake.random_int(1, 5)
        )
