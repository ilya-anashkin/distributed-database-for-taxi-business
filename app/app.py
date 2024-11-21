from fastapi import FastAPI

from api.routers.router import router


def init_routers(fastapi_app: FastAPI):
    fastapi_app.include_router(router)


def create_app() -> FastAPI:
    fastapi_app = FastAPI(
        title='API',
        version='1.0.0'
    )

    init_routers(fastapi_app=fastapi_app)

    return fastapi_app


app = create_app()
