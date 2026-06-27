from datetime import datetime
from beanie import Document
from pydantic import Field
from pymongo import IndexModel, ASCENDING
class Like(Document):
    user_id: str
    post_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "likes"

        indexes = [
            IndexModel(
                [
                    ("user_id", ASCENDING),
                    ("post_id", ASCENDING),
                ],
                unique=True,
                name="unique_user_post",
            )
        ]