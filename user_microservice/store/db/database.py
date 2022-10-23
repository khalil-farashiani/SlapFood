from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import get_settings



def _init_session():
    setting = get_settings()
    db = create_engine(url=setting.SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(autocommit=False, autoflush=True, bind=db)
    return session

SessionLocal = _init_session

