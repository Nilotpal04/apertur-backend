from pydantic import BaseModel

class LikeResponse(BaseModel):
    liked: bool
    likes_count: int
    liked_by_user: bool | None