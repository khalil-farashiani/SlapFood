from functools import lru_cache

from fastapi import FastAPI

from routers.apiv1 import user_router
from config import Setting


@lru_cache()
def get_settings():
    return Setting()


setting = get_settings()


def create_app():
    user_app = FastAPI(name=setting.APP_NAME, debug=setting.DEBUG)
    user_app.include_router(user_router)
    return user_app


app = create_app()
