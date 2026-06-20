from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class  UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    bio: str | None = None
    avatar_url: str | None = None
    
    created_at: datetime
    