from datetime import datetime
from pydantic import BaseModel

class AtlasPostResponse(BaseModel):
    post_id: str
    username: str
    avatar_url: str | None = None
    image_url: str | None = None
    
    latitude: float
    longitude: float
    location_name: str
    
    created_at: datetime