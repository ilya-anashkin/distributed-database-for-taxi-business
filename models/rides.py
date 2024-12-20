from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, Float
from core.config import Base, fake, NodeType, current_node_type


class RidesModel(Base):
    __tablename__ = "rides"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    car_rent_id = Column(Integer, ForeignKey("car_rents.id"), nullable=False)
    price = Column(Float, nullable=False)
    order_date = Column(Date, nullable=False)
    start_date = Column(Date)
    finish_date = Column(Date)
    from_latitude = Column(Float, nullable=False)
    from_longitude = Column(Float, nullable=False)
    to_latitude = Column(Float, nullable=False)
    to_longitude = Column(Float, nullable=False)
    client_feedback_stars = Column(SmallInteger)
    client_feedback_review = Column(String(500))
    driver_feedback_stars = Column(SmallInteger)

    @staticmethod
    def fake(i) -> RidesModel:
        if current_node_type == NodeType.MASTER:
            raise RuntimeError("Master node cannot fill RidesModel")

        shift = 0
        if current_node_type == NodeType.REPLICA2:
            shift = 1000
        return RidesModel(
            id=i + shift,
            client_id=fake.random_int(1, 10),
            car_rent_id=fake.random_int(1 + shift, 10 + shift),
            price=fake.random_int(10, 100),
            order_date=fake.date(),
            start_date=fake.date(),
            finish_date=fake.date(),
            from_latitude=fake.latitude(),
            from_longitude=fake.longitude(),
            to_latitude=fake.latitude(),
            to_longitude=fake.longitude(),
            client_feedback_stars=fake.random_int(1, 5),
            client_feedback_review=fake.text(),
            driver_feedback_stars=fake.random_int(1, 5),
        )
