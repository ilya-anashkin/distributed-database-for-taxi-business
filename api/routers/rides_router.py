from fastapi import APIRouter
from core.config import session
from models.rides import RidesModel
from sqlalchemy import func

router = APIRouter(prefix="/rides")


@router.get("/total_price")
async def get_total_price(id: int):
    result = (
        session.query(
            func.sum(RidesModel.price).label("total_price"), RidesModel.car_rent_id
        )
        .filter(RidesModel.car_rent_id == id)
        .group_by(RidesModel.car_rent_id)
        .first()
    )

    if result:
        return {"id": result.car_rent_id, "total_price": result.total_price}
    else:
        return {"total_price": 0, "id": id}
