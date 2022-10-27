from pydantic import BaseModel, Field, Extra
from typing import Optional

class UserLoginResponse(BaseModel):
    email: Optional[str]  = Field(description="name of user system")
    access_token: str    = Field(description="user access token")
    refresh_token: str   = Field(description="user refresh token")

    class Config:
        orm_mode = True

class UserLoginRequest(BaseModel):
    email : str    = Field(description="email of user system this is a required field")
    password : str = Field(description="password of user system")

    class Config:
        extra = Extra.forbid
        