from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    content: str
    image_url: str | None = None
    
class PostResponse(BaseModel):
    id: str
    content: str
    image_url: str | None = None
    created_at: datetime