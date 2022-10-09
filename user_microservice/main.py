from fastapi import FastAPI
from sqlalchemy.orm import declarative_base
from routers.apiv1 import user_router


def create_app():
    app = FastAPI(name=__name__)
    app.include_router(user_router)
    return app


app = create_app()

Base = declarative_base()
# settings = get_config(os.getenv("ENV") or "test")
# SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
