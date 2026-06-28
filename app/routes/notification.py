from fastapi import APIRouter

from app.dependencies.auth import CurrentUser

from app.schemas.notification import (
    NotificationResponse,
    MarkNotificationReadResponse
)

from app.services.notification import (
    get_notifications_service,
    mark_notification_read_service
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.get(
    "",
    response_model=list[NotificationResponse]
)
async def get_notifications(
    current_user: CurrentUser
):
    return await get_notifications_service(
        current_user
    )


@router.patch(
    "/{notification_id}/read",
    response_model=MarkNotificationReadResponse
)
async def mark_notification_read(
    notification_id: str,
    current_user: CurrentUser
):
    return await mark_notification_read_service(
        notification_id,
        current_user
    )