from fastapi import APIRouter
from models.apiv1 import User
from sqlalchemy.orm import Session
from store.db.postgresql import db_engine

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/{user_pk}")
def get_user(user_pk: str):
    session = Session(db_engine)
    user = session.get(User, user_pk)
    return {"error": user}


@user_router.post("/")
def create_user():
    return {"error": "emplement me!!"}
