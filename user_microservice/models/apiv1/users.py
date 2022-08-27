from xmlrpc.client import DateTime
from sqlalchemy import Column, String, Integer, DateTime
from user_microservice.main import Base


class User(Base):
    __tablename__ = 'users'    
    id                = Column(String(64), primary_key=True, default=uuidgen)
    username          = Column(String(128), unique=True, index=True, nullable=False)
    password          = Column(String(256), nullable=False)
    role              = Column(String(32), nullable=False, default=Config.USER_DEFUALT_ROLE)
    created_at        = Column(DateTime, nullable=False, default=now )
    expires_at        = Column(DateTime, nullable=False, default=user_expires_at)
    last_login_at     = Column(DateTime)
    last_active_at    = Column(DateTime)
    last_change_at    = Column(DateTime)
    failed_auth_at    = Column(DateTime)
    failed_auth_count = Column(Integer, default=0)
    status            = Column(Integer, nullable=False, default=Config.USER_DEFUALT_STATUS)