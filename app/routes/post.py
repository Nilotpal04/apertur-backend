from fastapi import APIRouter
from app.schemas.post import (
    PostCreate,
    PostResponse,
    PostUpdate
)
from app.services.post_service import (
    create_post_service,
    get_post_service,
    update_post_service,
    delete_post_service
)
from app.schemas.like import LikeResponse
from app.services.like_service import (
    like_post_service,
    unlike_post_service
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

@router.patch("/{post_id}", response_model=PostResponse)
async def update_post(
    post_id: str,
    post_data: PostUpdate,
    current_user: CurrentUser
):
    return await update_post_service(
        post_id,
        post_data,
        current_user
    )
    
@router.delete("/{post_id}")
async def delete_post(
    post_id: str,
    current_user: CurrentUser
):
    return await delete_post_service(
        post_id,
        current_user
    )
    
@router.post(
    "/{post_id}/like",
    response_model=LikeResponse
)
async def like_post(
    post_id: str,
    current_user: CurrentUser
):
    return await like_post_service(
        post_id,
        current_user
    )
    
@router.delete(
    "/{post_id}/like",
    response_model=LikeResponse
)
async def unlike_post(
    post_id: str,
    current_user: CurrentUser
):
    return await unlike_post_service(
        post_id,
        current_user
)