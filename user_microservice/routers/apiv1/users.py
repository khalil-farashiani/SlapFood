from fastapi import APIRouter
from store.db import get_user_data

user_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/{user_pk}")
def get_user(user_pk: str):
    get_user_data(user_pk)
    return {"error": "Null"}


@user_router.post("/")
def create_user():
    return {"error": "implement me!!"}
