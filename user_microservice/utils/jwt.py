import os
from datetime import datetime, timedelta
from typing import Any
from jose import jwt
from config import get_settings

settings = get_settings()

ACCESS_TOKEN_EXPIRE_MINUTES = settings.USER_DEFAULT_TOKEN_EXPIRY_TIME  #minutes
REFRESH_TOKEN_EXPIRE_MINUTES = settings.USER_DEFAULT_EXPIRES  #days
ALGORITHM = settings.USER_DEFAULT_TOKEN_ALGO  #like HS256 
JWT_SECRET_KEY = settings.SECRET_KEY   #should be kept secret
JWT_REFRESH_SECRET_KEY = settings.REFRESH_TOKEN_SECRET_KEY   # should be kept secret


def create_access_token(subject: str|Any, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: str|Any, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt