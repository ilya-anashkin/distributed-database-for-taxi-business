from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session
from core.config import session
from models.rides import RidesModel
from models.drivers import DriversModel
from models.drivers_states import DriversStatesModel
from models.drivers_statuses import DriversStatusesModel
from models.car_rents import CarRentsModel
from models.cars import CarsModel
from models.car_models_rbi import CarModelsRBIModel
from models.car_models import CarModelsModel
import datetime
from sqlalchemy import func

from schemas.common import Record

router = APIRouter(prefix='/drivers')


@router.get('/history', response_model=List[Record])
async def get_history(id: int):
    result = (
        session.query(
            RidesModel.id,
            RidesModel.price,
            RidesModel.order_date,
            RidesModel.client_feedback_stars,
            RidesModel.client_feedback_review,
        )
        .join(CarRentsModel, CarRentsModel.id == RidesModel.car_rent_id)
        .filter(CarRentsModel.driver_id == id)
        .all()
    )

    records: List[Record] = [
        Record(id=item[0], price=item[1], order_date=item[2], client_feedback_stars=item[3], client_feedback_review=item[4])
        for item in result
    ]

    return records

@router.get("/rents_history")
async def get_car_info(id: int):
    result = (
        session.query(
            CarModelsModel.model,
            CarsModel.vin_number,
            CarsModel.register_date,
            CarsModel.unregister_date,
        )
        .join(CarModelsRBIModel, CarsModel.car_model_rbi_id == CarModelsRBIModel.id)
        .join(CarModelsModel, CarModelsRBIModel.model_id == CarModelsModel.id)
        .join(CarRentsModel, CarRentsModel.car_id == CarsModel.id)
        .filter(CarRentsModel.driver_id == id)
        .all()
    )

    return result

@router.get('/current_taxi_pool')
async def get_current_taxi_pool(id: int):
    result = (
        session.query(
            CarsModel.taxi_pool_id,
            CarRentsModel.driver_id,
            CarsModel.vin_number,
            CarsModel.register_date,
            CarsModel.unregister_date,
        )
        .join(CarRentsModel, CarRentsModel.car_id == CarsModel.id)
        .filter(CarRentsModel.driver_id == id)
        .all()
    )

    return result

@router.get('/registered_before')
async def get_registered_before(date: str):
    result = (
        session.query(DriversModel)
        .filter(
            DriversModel.register_date < datetime.datetime.strptime(date, "%Y-%m-%d")
        )
        .all()
    )

    return result

@router.get('/with_status')
async def get_with_status(status: int, employment_status: int):
    result = (
        session.query(DriversModel)
        .join(DriversStatesModel, DriversStatesModel.driver_id == DriversModel.id)
        .filter(
            DriversStatesModel.status_id == status,
            DriversModel.employment_status_id == employment_status,
        )
        .all()
    )

    return result

@router.get('/with_high_rating')
async def get_with_high_rating(rating: int):
    result = (
        session.query(
            DriversModel.taxi_pool_id, func.count(DriversModel.id).label("count")
        )
        .join(RidesModel, RidesModel.driver_id == DriversModel.id)
        .filter(RidesModel.client_feedback_stars >= rating)
        .group_by(DriversModel.taxi_pool_id)
        .all()
    )

    return result
