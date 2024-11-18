from fastapi import APIRouter
from api.routers.insert_router import router as create_table_router

router = APIRouter()

router.include_router(create_table_router, prefix="/create_table")
