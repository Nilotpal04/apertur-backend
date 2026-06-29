from fastapi import APIRouter
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UpdateProfileRequest,
    PublicUserResponse,
    UserSearchResponse
)
from app.services.user_service import (
    register_user_service, 
    update_profile_service,
    get_user_profile_service,
    get_current_user_service,
    search_users_service
)
from app.services.follow_service import (
    follow_user_service,
    unfollow_user_service
)

from app.schemas.follow import FollowResponse
from app.schemas.post import PostResponse
from app.services.post_service import get_user_posts_service

from app.dependencies.auth import (
    CurrentUser,
    OptionalCurrentUser
)

from app.services.frame_service import (
    get_user_frames_service
)

from app.schemas.feed import FeedPostResponse


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
async def register_user(user_data: UserCreate):
    return await register_user_service(user_data)
    
@router.patch("/me", response_model=UserResponse)
async def update_profile(
    profile_data: UpdateProfileRequest,
    current_user: CurrentUser
):
    return await update_profile_service(
        current_user,
        profile_data
    )
    
@router.get("/search",response_model=list[UserSearchResponse])
async def search_users(q: str):
        return await search_users_service(q)
    
@router.get("/{username}", response_model=PublicUserResponse)
async def get_user_profile(
    username: str,
    current_user: OptionalCurrentUser
):    
    return await get_user_profile_service(
        username,
        current_user
    )
    
@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: CurrentUser
):
    return await get_current_user_service(
        current_user
    )

@router.get("/{username}/posts", response_model=list[PostResponse])
async def get_user_posts(username: str):
    return await get_user_posts_service(username)

@router.post("/{username}/follow", response_model=FollowResponse)
async def follow_user(
    username: str,
    current_user: CurrentUser
):
    return await follow_user_service(
        username,
        current_user
    )

@router.delete("/{username}/follow", response_model=FollowResponse)
async def unfollow_user(
    username: str,
    current_user: CurrentUser
):
    return await unfollow_user_service(
        username,
        current_user
    )

@router.get(
    "/{username}/frames",
    response_model=list[FeedPostResponse]
)
async def get_user_frames(
    username: str
):
    return await get_user_frames_service(
        username
    )