from fastapi import APIRouter, Depends, HTTPException
from dependency import get_token_header

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/{user_id}")
def get_user(user_id: int):
    return {"error": "implement me!!"}


@user_router.post("/")
def create_user():
    return {"error": "emplement me!!"}