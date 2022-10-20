from models.apiv1 import User
from sqlalchemy.orm import Session
from store.db.init import db_engine


def get_user_data(user_id: str):
    session = Session(db_engine)
    user = session.get(User, user_id)
    return user
