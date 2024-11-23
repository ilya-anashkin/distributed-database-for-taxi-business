from fastapi import APIRouter
from sqlalchemy.orm import Session
from core.config import session
from models.rides import RidesModel
from models.drivers import DriversModel
from models.drivers_states import DriversStatesModel
from models.drivers_statuses import DriversStatusesModel
from models.car_rents import CarRentsModel
from models.cars import CarsModel
from models.car_models_rbi import CarModelsRbiModel
from models.car_models import CarModelsModel
import datetime
from sqlalchemy import func

router = APIRouter()

@router.get('/total_price')
async def get_total_price(id: int):
	result = session.query(
		func.sum(RidesModel.price).label('total_price'),
		RidesModel.car_rent_id
	).group_by(RidesModel.car_rent_id).all()

	return result
