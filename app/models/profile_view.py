from datetime import datetime
from beanie import Document
from pydantic import Field

class ProfileView(Document):
    profile_id: str
    viewed_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name: "profile_views"