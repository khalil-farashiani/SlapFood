from functools import lru_cache

from fastapi import FastAPI

from routers.apiv1 import user_router
from config import get_settings


setting = get_settings()


def create_app():
    user_app = FastAPI(name=setting.APP_NAME, debug=setting.DEBUG)
    user_app.include_router(user_router)
    return user_app


app = create_app()
