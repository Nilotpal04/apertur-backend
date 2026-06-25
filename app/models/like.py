from datetime import datetime
from beanie import Document
from pydantic import Field

class Like(Document):
    user_id: str
    post_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "likes"
        
        indexes = [
            [
                ("user_id", 1),
                ("post_id", 1),
            ],
            {
                "name": "unique_user_post",
                "unique": True,
            }
        ]