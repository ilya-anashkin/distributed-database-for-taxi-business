from fastapi import APIRouter
from core.config import session
from models.cars import CarsModel
from sqlalchemy import func

router = APIRouter()

@router.get('/no_inspection')
async def get_cars_no_inspection(years: int):
	result = session.query(CarsModel).filter(
		func.extract('year', func.age(func.now(), CarsModel.last_inspection_date)) > years
	).all()

	return result
