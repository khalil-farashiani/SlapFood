from pydantic import BaseModel, Extra, Field 
from typing import Optional

class User(BaseModel):
    real_name : Optional[str] = Field(description="name of user system")
    email : str          = Field(description="email of user system this is a required field") 
    active : bool        = Field(default=False, description="is user active or not")
    user_password : str  = Field(description="user password")
    score : int          = Field(default=0, description="user score")
    address : str        = Field(description="user address this is a foreinkey to address table")
    user_role : str      = Field(description="role of user like common user or seller this is many to many field to role table")


    class Config:
        extra = Extra.forbid
        orm_mode = True

class GetUser(BaseModel):
    email : str               = Field(description="email of user system this is a required field") 
    status : int              = Field(default=False, description="is user active or not")
    real_name : Optional[str] = Field(description="name of user system")
    mobile : Optional[str]    = Field(description="mobile of user system")
    user_role : str           = Field(description="role of user like common user or seller this is many to many field to role table")


    class Config:
        extra = Extra.forbid
        orm_mode = True

class CreateUSerRequest(BaseModel):
    real_name : Optional[str] = Field(description="name of user system")
    email : str               = Field(description="email of user system this is a required field") 
    user_password : str       = Field(description="user password")
    address : Optional[str]   = Field(description="user address this is a foreinkey to address table")
    mobile : Optional[str]    = Field(description="mobile number of user")

    class Config:
        extra = Extra.forbid


class CreateUSerResponse(BaseModel):
    real_name : Optional[str] = Field(description="name of user system")
    email : str               = Field(description="email of user system this is a required field") 
    address : Optional[str]   = Field(description="user address this is a foreinkey to address table")
    mobile : Optional[str]    = Field(description="mobile number of user")


    class Config:
        orm_mode = True