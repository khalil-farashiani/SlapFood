from fastapi import APIRouter, Depends, HTTPException
from dependency import get_token_header

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/")
def get_user():
    return {"error": "emplement me!!"}


@user_router.post("/{user_id}")
def create_user(user_id: int):
    return {"message": user_id, "error": "emplement me!!"}