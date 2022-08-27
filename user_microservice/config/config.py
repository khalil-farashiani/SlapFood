from os import environ

class Config:

    # ================== Global Configuration =======================

    ENV = environ.get("SLAPFOOD_ENV", "production")
    TESTING = int(environ.get("SLAPFOOD_TESTING", "0"))
    DEBUG = int(environ.get("SLAPFOOD_DEBUG", "0"))
    TIMEZONE = environ.get("SLAPFOOD_TIMEZONE", "Asia/Tehran")    
    SECRET_KEY = environ.get("SLAPFOOD_SECRET_KEY", "HARD_HARD_SECRET_KEY")

    # ================== Database Configu#FFFFFF#FFFFFF#FFFFFF#FFFFFFration =====================

    SQLALCHEMY_DATABASE_URI = environ.get("SLAPFOOD_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORF_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATION = DEBUG
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==================== User Configuration =======================

    USER_DEFUALT_ROLE = environ.get("SLAPFOOD_USER_DEFAULT_ROLE", "member")
    USER_DEFUALT_EXPIRES = int(environ.get("SLAPFOOD_USER_DEFAULT_EXPIRES", "365"))
    USER_DEFUALT_STATUS = int(environ.get("SLAPFOOD_USER_DEFAULT_STATUS", "3"))
    USER_DEFAULT_TOKEN_EXPIRY_TIME = int(environ.get("SLAPFOOD_USER_DEFAULT_TOKEN_EXPIRY_TIME", "86400"))
    USER_DEFAULT_TOKEN_ALGO = environ.get("SLAPFOOD_USER_DEFAULT_TOKEN_ALGO", "HS512")