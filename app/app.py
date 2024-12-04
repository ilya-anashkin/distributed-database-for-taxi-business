from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers.router import router
from api.routers.drivers_router import router as drivers_router
from api.routers.cars_router import router as cars_router
from api.routers.rides_router import router as rides_router


def init_routers(fastapi_app: FastAPI):
    fastapi_app.include_router(router)
    fastapi_app.include_router(drivers_router)
    fastapi_app.include_router(cars_router)
    fastapi_app.include_router(rides_router)


def create_app() -> FastAPI:
    fastapi_app = FastAPI(title="API", version="1.0.0")

    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    init_routers(fastapi_app=fastapi_app)

    return fastapi_app


app = create_app()
