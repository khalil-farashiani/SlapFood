from fastapi import FastAPI
from typing import Union

def create_app():
    app = FastAPI(name= __name__)
    return app



app = create_app()


@app.get("/users")
async def read_item():
    return {"users": ["ali", "test"]}