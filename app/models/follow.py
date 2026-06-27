from datetime import datetime
from beanie import Document
from pydantic import Field
from pymongo import IndexModel, ASCENDING

class Follow(Document):
    follower_id: str
    following_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Settings:
        name = "follows"

        indexes = [
            IndexModel(
                [
                    ("follower_id", ASCENDING),
                    ("following_id", ASCENDING),
                ],
                unique=True,
                name="unique_follower_following",
            )
        ]