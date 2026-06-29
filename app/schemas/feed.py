from pydantic import BaseModel

class FeedPostResponse(BaseModel):
    id: str
    username: str
    avatar_url: str | None = None
    content: str | None = None
    image_url: str | None = None
    likes_count: int
    liked_by_user: bool | None = None
    
    latitude: float | None = None
    longitude: float | None = None
    location_name: str | None = None
class FeedResponse(BaseModel):
    posts: list[FeedPostResponse]
    next_cursor: str | None = None