from datetime import datetime
from beanie import Document
from pydantic import Field

from app.enums.notification_type import NotificationType

class Notification(Document):
    recipient_id: str
    actor_id: str
    post_id: str | None = None
    notification_type: NotificationType
    is_read: bool = False
    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )
    class Settings:
        name = "notifications"