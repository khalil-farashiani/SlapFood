import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from config.config import get_settings
from sqlalchemy.orm import declarative_base

base = declarative_base()


class User(base):
    __tablename__: str = 'users'
    id                = Column(String(64), primary_key=True, default=uuid.uuid4)
    email             = Column(String(128), unique=True, index=True, nullable=False)
    real_name         = Column(String(256), nullable=True)
    mobile            = Column(String(256), nullable=True)
    user_password     = Column(String(256), nullable=False)
    user_role         = Column(String(32), nullable=False, default=get_settings().USER_DEFAULT_ROLE)
    created_at        = Column(DateTime, nullable=False, default=datetime.now)
    expires_at        = Column(DateTime, nullable=False, default=get_settings().USER_DEFAULT_TOKEN_EXPIRY_TIME)
    failed_auth_at    = Column(DateTime)
    failed_auth_count = Column(Integer, default=0)
    status            = Column(Integer, nullable=False, default=get_settings().USER_DEFAULT_STATUS)

    def __repr__(self):
        return f"<User {self.email}"
