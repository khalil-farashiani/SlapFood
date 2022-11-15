from fastapi import APIRouter, Depends, HTTPException
from store.db import get_user, get_user_by_email,  make_user
from schema.apiv1.users import GetUser, CreateUSerRequest, CreateUSerResponse
from sqlalchemy.orm import Session
from dependency import get_db
from models.apiv1 import User
from utils.password import get_hashed_password

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/{user_pk}", response_model=GetUser)
async def read_user(user_pk: str, db: Session = Depends(get_db)):
    user = get_user(db, user_pk)
    if user is None:
        return HTTPException(404, detail="Not found")
    return user

@user_router.post("/")
async def create_user(data: CreateUSerRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, data.email)
    if user is not None:
        return HTTPException(400, detail="email already taken")
    user = User(
        email=data.email,
        real_name=data.real_name,
        user_password=get_hashed_password(data.user_password),
        mobile=data.mobile,
        address=data.address
    )
    try:
        make_user(db, user)
    except:
        raise HTTPException(500, detail="unable to create user")
    return {
        "status_code": 200,
        "message": "user successfully create",
    }