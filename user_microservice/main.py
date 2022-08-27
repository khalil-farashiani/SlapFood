from curses import echo
from fastapi import FastAPI
from typing import Union
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

def create_app():
    app = FastAPI(name= __name__)
    # get from ENV 
    engine = create_engine(
        "dsn",
        echo=False,
    )

Base = declarative_base()
# settings = get_config(os.getenv("ENV") or "test")
# SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
