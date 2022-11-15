from models.apiv1 import User
from sqlalchemy import exc
from sqlalchemy.orm import Session


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def make_user(db: Session, user: User) -> None:
    try:
        db.add(user)
        db.commit()
    except exc.SQLAlchemyError as e:
        raise e