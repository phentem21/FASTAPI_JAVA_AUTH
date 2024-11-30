from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    roles: Optional[list[str]] = ["user"]

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
