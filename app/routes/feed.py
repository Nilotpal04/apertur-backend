from fastapi import APIRouter
from app.schemas.feed import (
    FeedResponse
)

from app.services.feed_service import get_feed_service

router = APIRouter(
    prefix="/feed",
    tags=["Feed"]
)

@router.get("", response_model=FeedResponse)
async def get_feed():
    return await get_feed_service()