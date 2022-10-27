from functools import lru_cache

from fastapi import FastAPI

from routers.apiv1 import user_router, auth_router
from config import get_settings
from dependency import create_tables

setting = get_settings()


def create_app():
    user_app = FastAPI(name=setting.APP_NAME, debug=setting.DEBUG)
    user_app.include_router(user_router)
    user_app.include_router(auth_router)
    create_tables()
    return user_app


app = create_app()
