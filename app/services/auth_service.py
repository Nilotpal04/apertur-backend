from app.models.user import User
from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

from app.core.security import verify_password
from app.core.auth import (
    create_access_token,
    create_refresh_token,
    decode_token
)

from app.exceptions.auth_exceptions import (
    InvalidCredentialsException
)

async def login_user_service( login_data: LoginRequest ) -> TokenResponse:
    user = await User.find_one(
        User.email == login_data.identifier
    )
    
    if not user:
        user = await User.find_one(
            User.username == login_data.identifier
        )
    
    if not user:
        raise InvalidCredentialsException()
    
    if not verify_password(
        login_data.password,
        user.hashed_password
    ):
        raise InvalidCredentialsException()
    
    access_token = create_access_token(
        str(user.id)
    )
    
    refresh_token = create_refresh_token(
        str(user.id)
    )
    
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token
    )
    
async def refresh_token_service( refresh_token: str ):
    payload = decode_token(refresh_token)
    
    if payload.get("type") != "refresh":
        raise InvalidCredentialsException()
    
    user_id = payload.get("sub")
    user = await User.get(user_id)
    
    access_token = create_access_token(str(user_id))
    
    return {
        "access_token": access_token
    }