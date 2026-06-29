from fastapi import APIRouter

from app.schemas.atlas import AtlasPostResponse
from app.services.atlas_service import get_atlas_post_service

router = APIRouter(
    prefix="/atlas",
    tags=["Atlas"]
)

@router.get("", response_model=list[AtlasPostResponse])
async def get_atlas_post():
    return await get_atlas_post_service()