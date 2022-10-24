from pydantic import BaseModel, Field, Optional

class UserAuth(BaseModel):
    name: Optional[str]  = Field(description="name of user system")
    access_token: str    = Field(description="user access token")
    refresh_token: str   = Field(description="user refresh token")