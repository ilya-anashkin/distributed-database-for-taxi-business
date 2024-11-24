from __future__ import annotations

from sqlalchemy import Column, Integer, String
from core.config import Base, fake


class CarModelsModel(Base):
    __tablename__ = "car_models"
    id = Column(Integer, primary_key=True)
    model = Column(String(100), nullable=False, unique=True)

    @staticmethod
    def fake(i) -> CarModelsModel:
        return CarModelsModel(model=fake.word())
