from fastapi import Header, HTTPException
from store.db.database import SessionLocal, engine
from models.apiv1.users import base
# TODO: complete this section

async def get_token_header(x_token: str = Header()):
    if x_token != "PLEASE README FROM ENV":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "slapfood":
        raise HTTPException(status_code=400, detail="No slapfood token provided")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()

def create_tables():
    base.metadata.create_all(bind=engine)