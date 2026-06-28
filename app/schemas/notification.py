from datetime import datetime
from pydantic import BaseModel
from app.enums.notification_type import NotificationType

class NotificationResponse(BaseModel):
    id: str
    actor_username: str
    actor_avatar_url: str | None = None
    notification_type: NotificationType
    post_id: str | None = None
    is_read: bool
    created_at: datetime
    
class MarkNotificationReadResponse(BaseModel):
    success: bool