from fastapi import APIRouter
from app.schemas.feed import (
    FeedResponse
)

from app.services.feed_service import get_feed_service
from app.dependencies.auth import OptionalCurrentUser

router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)

@router.get("", response_model=FeedResponse)
async def get_feed( current_user: OptionalCurrentUser):
    return await get_feed_service( current_user=current_user )