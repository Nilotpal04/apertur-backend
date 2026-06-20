from app.models.user import User
from app.schemas.user import UserCreate
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