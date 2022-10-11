from pydantic import BaseSettings


class Setting(BaseSettings):
    # ================== Global Configuration =======================
    APP_NAME: str = "user_app"
    ENV: str = "production"
    TESTING: int = 0
    DEBUG: bool = True
    TIMEZONE: str = "Asia/Tehran"
    SECRET_KEY: str = "VERY_HARD_HARD_HARD_SECRET_KEY"

    # ================== Database Configuration =====================

    SQLALCHEMY_DATABASE_URI: str = None
    SQLALCHEMY_ECHO: bool = DEBUG

    # ==================== User Configuration =======================

    USER_DEFAULT_ROLE: str = "member"
    USER_DEFAULT_EXPIRES: int = 365
    USER_DEFAULT_STATUS: int = 3
    USER_DEFAULT_TOKEN_EXPIRY_TIME: int = 86400
    USER_DEFAULT_TOKEN_ALGO: str = "HS512"

    class Config:
        env_file = ".env"

    def get_sqlAlchemy_conf(self) -> dict:
        return {
            "url": self.SQLALCHEMY_DATABASE_URI,
            "echo": self.SQLALCHEMY_ECHO,
        }
