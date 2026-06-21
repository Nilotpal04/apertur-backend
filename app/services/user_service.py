from app.models.user import User
from datetime import datetime, timezone
from app.schemas.user import (
    UserCreate,
    UpdateProfileRequest
)
from app.exceptions.user_exception import (
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException
)
from app.core.security import hash_password

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