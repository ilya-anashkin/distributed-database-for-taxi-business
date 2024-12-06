from fastapi import APIRouter
from core.config import sessions
from models.cars import CarsModel
from sqlalchemy import func

router = APIRouter(prefix="/cars")


@router.get("/no_inspection")
async def get_cars_no_inspection(years: int, bd_id: str):
    session = sessions[bd_id]
    result = (
        session.query(CarsModel)
        .filter(
            func.extract("year", func.age(func.now(), CarsModel.last_inspection_date))
            > years
        )
        .all()
    )

    return result
