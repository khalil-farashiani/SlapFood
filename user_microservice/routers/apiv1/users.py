from fastapi import APIRouter, Depends, HTTPException
from dependency import get_token_header

user_router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@user_router.get("/{item_id}")
def create_user(item_id: int):
    return {"message": item_id, "error": "emplement me!!"}
