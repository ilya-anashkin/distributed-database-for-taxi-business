from datetime import date
from pydantic import BaseModel

class Record(BaseModel):
    id: int
    price: float
    order_date: date
    client_feedback_stars: int
    client_feedback_review: str

class PriceCarRent(BaseModel):
    id: int
    price: float