from __future__ import annotations

from sqlalchemy import Column, Integer, String
from core.config import Base, fake


class CarColorsModel(Base):
    __tablename__ = "car_colors"
    id = Column(Integer, primary_key=True)
    color = Column(String(100), nullable=False)

    @staticmethod
    def fake(i) -> CarColorsModel:
        return CarColorsModel(color=fake.color_name())
