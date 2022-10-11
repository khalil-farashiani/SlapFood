from functools import lru_cache

from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from sqlalchemy import engine_from_config

from routers.apiv1 import user_router
from . import config


@lru_cache()
def get_settings():
    return config.Setting()


db = engine_from_config(get_settings().get_sqlAlchemy_conf(), prefix="user")


def create_app():
    setting = get_settings()
    user_app = FastAPI(name=setting.APP_NAME, debug=setting.DEBUG)
    user_app.include_router(user_router)
    return user_app


app = create_app()

Base = declarative_base()
# settings = get_config(os.getenv("ENV") or "test")
# SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
