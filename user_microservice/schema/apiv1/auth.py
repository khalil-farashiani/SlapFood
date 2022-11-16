from pydantic import BaseModel, Field, Extra
from typing import Optional

class UserLoginRequest(BaseModel):
    email : str    = Field(description="email of user system this is a required field")
    password : str = Field(description="password of user system")

    class Config:
        extra = Extra.forbid
        