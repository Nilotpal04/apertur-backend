from datetime import datetime
from beanie import Document
from pydantic import Field

class User(Document):
    username: str
    email: str
    hashed_password: str
    
    name: str | None = None
    bio: str | None = None
    avatar_url: str | None = None
    
    is_active: bool = True
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class  Settings:
        name = "users"