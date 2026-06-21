from fastapi import APIRouter
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UpdateProfileRequest,
    PublicUserResponse
)
from app.services.user_service import (
    register_user_service, 
    update_profile_service,
    get_user_profile_service
)

from app.schemas.post import PostResponse
from app.services.post_service import get_user_posts_service

from app.dependencies.auth import CurrentUser

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
async def register_user(user_data: UserCreate):
    return await register_user_service(user_data)

@router.get("/me", response_model=UserResponse)
async def get_me( current_user: CurrentUser ):
    return UserResponse(
        id=str(current_user.id),
        username=current_user.username,
        email = current_user.email,
        bio=current_user.bio,
        avatar_url=current_user.avatar_url,
        created_at=current_user.created_at
    )
    
@router.patch("/me", response_model=UserResponse)
async def update_profile(
    profile_data: UpdateProfileRequest,
    current_user: CurrentUser
):
    return await update_profile_service(
        current_user,
        profile_data
    )
    
@router.get("/{username}", response_model=PublicUserResponse)
async def get_user_profile(username: str):
    
    user = await get_user_profile_service(username)
    
    return PublicUserResponse(
        username=user.username,
        name=user.name,
        bio=user.bio,
        avatar_url=user.avatar_url
    )

@router.get("/{username}/posts", response_model=list[PostResponse])
async def get_user_posts(username: str):
    return await get_user_posts_service(username)