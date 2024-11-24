from __future__ import annotations

from sqlalchemy import Column, Integer, String, ForeignKey, Date, SmallInteger, Float
from core.config import Base, fake

class EmploymentStatusesModel(Base):
    __tablename__ = 'employment_statuses'
    id = Column(Integer, primary_key=True)
    status = Column(String(50), nullable=False, unique=True)

    @staticmethod
    def fake() -> EmploymentStatusesModel:
        return EmploymentStatusesModel(
            status=fake.word()
        )
