from functools import lru_cache

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

from config import Setting


@lru_cache()
def get_settings():
    return Setting()


def _init_db():
    setting = get_settings()
    db = create_engine(url=setting.SQLALCHEMY_DATABASE_URI)
    return db


base = declarative_base()
db_engine = _init_db()
