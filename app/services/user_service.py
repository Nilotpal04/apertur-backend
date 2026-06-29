from app.models.user import User
from datetime import datetime, timezone
from app.schemas.user import (
    UserCreate,
    UpdateProfileRequest
)
from app.exceptions.user_exception import (
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException,
    UserNotFoundException
)
from app.core.security import hash_password
from app.models.follow import Follow
from app.schemas.user import (
    UserResponse,
    PublicUserResponse
)
from app.schemas.user import UserSearchResponse

async def register_user_service(user_data: UserCreate):
    
    existing_email = await User.find_one(
        User.email == user_data.email
    )
    
    if existing_email:
        raise EmailAlreadyExistsException()
    
    existing_username = await User.find_one(
        User.username == user_data.username
    )
    
    if existing_username:
        raise UsernameAlreadyExistsException()
    
    hashed_password = hash_password(
        user_data.password
    )

    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password
    )

    await user.insert()

    return {
        "message": "User created successfully"
    }

async def update_profile_service(
    user: User,
    profile_data: UpdateProfileRequest
):
    update_data = profile_data.model_dump(
        exclude_unset=True
    )
    
    for field, value in update_data.items():
        setattr(user, field, value)
    user.updated_at = datetime.now(timezone.utc)
    await user.save()
    
    return user

async def get_user_profile_service(
    username: str,
    current_user: User | None    
):
    user = await User.find_one(
        User.username == username
    )
    if not user:
        raise UserNotFoundException()
    
    followers_count = await Follow.find(Follow.following_id == str(user.id)).count()
    following_count = await Follow.find(Follow.follower_id == str(user.id)).count()
    is_following = None
    if current_user:
        follow = await Follow.find_one(
            Follow.follower_id == str(current_user.id),
            Follow.following_id == str(user.id)
        )
        is_following = follow is not None
        
    return PublicUserResponse(
        username=user.username,
        name=user.name,
        bio=user.bio,
        avatar_url=user.avatar_url,
        followers_count=followers_count,
        following_count=following_count,
        is_following=is_following
    )

async def get_current_user_service(
    current_user: User
):
    followers_count = await Follow.find(Follow.following_id == str(current_user.id)).count()

    following_count = await Follow.find(Follow.follower_id == str(current_user.id)).count()

    return UserResponse(
        id=str(current_user.id),
        username=current_user.username,
        email=current_user.email,
        bio=current_user.bio,
        avatar_url=current_user.avatar_url,
        created_at=current_user.created_at,
        followers_count=followers_count,
        following_count=following_count
    )
    
async def search_users_service(query: str):
    query = query.strip()
    if not query:
        return []
    if len(query) < 2:
        return []
    
    users = await User.find(
        {
            "username": {
                "$regex": query,
                "$options": "i"
            }
        }
    ).limit(20).to_list()
    
    return [
        UserSearchResponse(
            username=user.username,
            name=user.name,
            avatar_url=user.avatar_url
        )
        for user in users
    ]