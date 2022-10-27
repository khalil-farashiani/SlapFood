from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.apiv1.auth import (
    UserLoginRequest,
    UserLoginResponse,
    )
from dependency import get_db
from store.db.user_dao import get_user_by_email

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@auth_router.post("/login")
def login(data: UserLoginRequest, db: Session = Depends(get_db)):
    email = data.email
    user = get_user_by_email(db, email)
    if user is None:
        return HTTPException(404, detail="user not found")
    return {"access_token": "ok",  "refresh_token": "test"}