from __future__ import annotations

from sqlalchemy import Column, Integer, ForeignKey
from core.config import Base, fake


class CarModelsRBIModel(Base):
    __tablename__ = "car_models_rbi"
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey("car_models.id"), nullable=False)
    color_id = Column(Integer, ForeignKey("car_colors.id"), nullable=False)
    class_id = Column(Integer, ForeignKey("car_classes.id"), nullable=False)

    @staticmethod
    def fake(i) -> CarModelsRBIModel:
        return CarModelsRBIModel(
            model_id=fake.random_int(1, 10),
            color_id=fake.random_int(1, 10),
            class_id=fake.random_int(1, 10),
        )
