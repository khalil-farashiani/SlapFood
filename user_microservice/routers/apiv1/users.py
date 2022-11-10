from fastapi import APIRouter, Depends, HTTPException
from store.db import get_user
from schema.apiv1.users import GetUser
from sqlalchemy.orm import Session
from dependency import get_db

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/{user_pk}", response_model=GetUser)
def read_user(user_pk: str, db: Session = Depends(get_db)):
    user = get_user(db, user_pk)
    if user is None:
        return HTTPException(404, detail="Not found")
    return user

@user_router.post("/")
def create_user():
    return {"error": "implement me!!"}
