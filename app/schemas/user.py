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
    
    followers_count: int
    following_count: int
    
    created_at: datetime

class UpdateProfileRequest(BaseModel):
    name: str | None = None
    bio: str | None = None
    avatar_url: str | None = None
    
class PublicUserResponse(BaseModel):
    username: str
    name: str | None = None
    bio: str | None = None
    avatar_url: str | None = None
    
    followers_count: int
    following_count: int
    is_following: bool | None = None
    
class UserSearchResponse(BaseModel):
    username: str
    name: str | None = None
    avatar_url: str | None = None