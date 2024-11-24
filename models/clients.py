from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, Float
from core.config import Base, fake

class ClientsModel(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    register_date = Column(Date, nullable=False)
    disable_date = Column(Date)
    phone = Column(String(30), nullable=False, unique=True)
    rating = Column(SmallInteger, nullable=False)

    @staticmethod
    def fake() -> ClientsModel:
        return ClientsModel(
            name=fake.name(),
            register_date=fake.date(),
            disable_date=fake.date(),
            phone=fake.phone_number(),
            rating=fake.random_int(1, 100)
        )
