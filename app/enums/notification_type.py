from enum import Enum

class NotificationType(str, Enum):
    LIKE = "like"
    FOLLOW = "follow"
    FRAME = "frame"