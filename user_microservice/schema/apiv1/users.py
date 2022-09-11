from pydantic import BaseModel, Extra, Field 
from typing import Optional

class User(BaseModel):
    name : Optional[str]         = Field(description="name of user system")
    phone_number : Optional[str] = Field(description="phone number of user system")
    email : str                  = Field(description="email of user system this is a required field") 
    active : bool                = Field(default=False, description="is user active or not")
    password : str               = Field(description="user password")
    score : int                  = Field(default=0, description="user score")
    address : str                = Field(description="user address this is a foreinkey to address table")
    role : str                   = Field(description="role of user like common user or seller this is many to many field to role table")


    class Config:
        extra = Extra.Forbid