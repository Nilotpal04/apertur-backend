from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    content: str
    image_url: str | None = None
    
    latitude: float | None = None
    longitude: float | None = None
    location_name: str | None = None
    
class PostResponse(BaseModel):
    id: str
    content: str
    image_url: str | None = None
    created_at: datetime
    
    latitude: float | None = None
    longitude: float | None = None
    location_name: str | None = None

class PostUpdate(BaseModel):
    content: str | None = None

    latitude: float | None = None
    longitude: float | None = None
    location_name: str | None = None