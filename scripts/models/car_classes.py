from __future__ import annotations

from sqlalchemy import Column, Integer, String
from config import Base, fake

class CarClassesModel(Base):
    __tablename__ = 'car_classes'
    id = Column(Integer, primary_key=True)
    car_class = Column(String(100), nullable=False, unique=True)

    @staticmethod
    def fake() -> CarClassesModel:
        return CarClassesModel(car_class=fake.word())
