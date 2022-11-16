from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.apiv1.auth import (
    UserLoginRequest,
    )
from dependency import get_db
from store.db.user_dao import get_user_by_email
from utils.jwt import create_access_token, create_refresh_token
from utils.password import verify_password
from utils.error import RestError
auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@auth_router.post("/login")
async def login(data: UserLoginRequest, db: Session = Depends(get_db)):
    email = data.email
    user = get_user_by_email(db, email)
    if user is None:
        error = RestError(error="username or password is incorrect", external_status=400, status=400)
        raise HTTPException(404, detail=error)
    hashed_pass = user.password
    if not verify_password(data.password, hashed_pass):
        error = RestError(error="username or password is incorrect", external_status=400, status=400)
        raise HTTPException(400,detail=error)
    return {
        "internal_status_code": 200,
        "external_status_code": 200,
        "access_token": create_access_token(user['email']),
        "refresh_token":  create_refresh_token(user['email']),
    }