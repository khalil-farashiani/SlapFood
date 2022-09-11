from fastapi import Header, HTTPException


# TODO: complete this section

async def get_token_header(x_token: str = Header()):
    if x_token != "PLEASE README FROM ENV":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "slapfood":
        raise HTTPException(status_code=400, detail="No slapfood token provided")
