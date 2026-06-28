from app.models.notification import Notification
from app.enums.notification_type import NotificationType
from app.models.user import User
from app.schemas.notification import NotificationResponse
from app.exceptions.notification_exceptions import NotificationNotFoundException
from beanie.operators import In
from beanie import PydanticObjectId

async def create_notification_service(
    recipient_id: str,
    actor_id: str,
    notification_type: NotificationType,
    post_id: str | None = None
):
    if recipient_id == actor_id:
        return
    notification = Notification(
        recipient_id=recipient_id,
        actor_id=actor_id,
        notification_type=notification_type,
        post_id=post_id
    )
    
    await notification.insert()
    
async def get_notifications_service(
    current_user: User
):
    notifications = await Notification.find(Notification.recipient_id == str(current_user.id)
    ).sort(
        -Notification.created_at
    ).to_list()

    if not notifications:
        return []

    actor_ids = {PydanticObjectId(notification.actor_id) for notification in notifications}

    users = await User.find(In(User.id, list(actor_ids))).to_list()

    users_map = {
        str(user.id): user
        for user in users
    }

    response: list[NotificationResponse] = []

    for notification in notifications:
        actor = users_map.get(notification.actor_id)

        if not actor:
            continue

        response.append(
            NotificationResponse(
                id=str(notification.id),
                actor_username=actor.username,
                actor_avatar_url=actor.avatar_url,
                notification_type=notification.notification_type,
                post_id=notification.post_id,
                is_read=notification.is_read,
                created_at=notification.created_at,
            )
        )

    return response

async def mark_notification_read_service(
    notification_id: str,
    current_user: User
):
    notification = await Notification.get(notification_id)
    if not notification:
        raise NotificationNotFoundException()