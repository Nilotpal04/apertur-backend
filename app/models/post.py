from datetime import datetime
from beanie import Document
from pydantic import Field

class Post(Document):
    author_id: str
    content: str
    image_url: str | None = None
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name = "posts"