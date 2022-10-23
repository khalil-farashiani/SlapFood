from models.apiv1 import User
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()
