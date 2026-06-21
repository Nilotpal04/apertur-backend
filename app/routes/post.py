from fastapi import APIRouter
from app.schemas.post import (
    PostCreate,
    PostResponse
)
from app.services.post_service import (
    create_post_service,
    get_post_service
)
from app.dependencies.auth import CurrentUser

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post( "", response_model=PostResponse)
async def create_post(post_data: PostCreate, current_user: CurrentUser):
    return await create_post_service(
        post_data,
        current_user
    )

@router.get(
    "/{post_id}",
    response_model=PostResponse
)
async def get_post(
    post_id: str
):
    return await get_post_service(
        post_id
    )
