from typing import List

from fastapi import APIRouter
from core.config import session
from models.rides import RidesModel
from sqlalchemy import func

from schemas.common import PriceCarRent

router = APIRouter(prefix='/rides')

@router.get('/total_price', response_model=List[PriceCarRent])
async def get_total_price():
	result = session.query(
		func.sum(RidesModel.price).label('total_price'),
		RidesModel.car_rent_id
	).group_by(RidesModel.car_rent_id).all()

	records: List[PriceCarRent] = [
		PriceCarRent(id=item[1], price=item[0])
		for item in result
	]

	return records
