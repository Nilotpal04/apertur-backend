from datetime import datetime
from beanie import Document
from pydantic import Field

class Frame(Document):
    user_id: str
    post_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name = "frames"