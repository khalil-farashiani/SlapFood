from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import get_settings



def _init_session():
    setting = get_settings()
    engine = create_engine(url=setting.SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    return session, engine

SessionLocal, engine = _init_session()

