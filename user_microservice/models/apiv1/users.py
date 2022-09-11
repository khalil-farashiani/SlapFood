import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from user_microservice.main import Base


class User(Base):
    __tablename__ = 'users'    
    id                = Column(String(64), primary_key=True, default=uuid.uuid4)
    username          = Column(String(128), unique=True, index=True, nullable=False)
    password          = Column(String(256), nullable=False)
    role              = Column(String(32), nullable=False, default=Config.USER_DEFUALT_ROLE)
    created_at        = Column(DateTime, nullable=False, default=datetime.now)
    expires_at        = Column(DateTime, nullable=False, default=config.USER_EXPIRATION)
    last_login_at     = Column(DateTime)
    last_active_at    = Column(DateTime)
    last_change_at    = Column(DateTime)
    failed_auth_at    = Column(DateTime)
    failed_auth_count = Column(Integer, default=0)
    status            = Column(Integer, nullable=False, default=Config.USER_DEFUALT_STATUS)