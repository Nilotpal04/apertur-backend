from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from typing import Annotated
from fastapi import Depends

from app.models.user import User
from app.core.auth import decode_token
from app.exceptions.auth_exceptions import (
    InvalidCredentialsException
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)
TokenDep = Annotated[
    str,
    Depends(oauth2_scheme)
]

async def get_current_user( token: TokenDep):
    try:
        payload = decode_token(token)
    except JWTError:
        raise InvalidCredentialsException()
    
    user_id = payload.get("sub")
    
    if not user_id:
        raise InvalidCredentialsException()
    
    user = await User.get(user_id)
    if not user:
        raise InvalidCredentialsException()
    
    return user

CurrentUser = Annotated[
    User,
    Depends(get_current_user)
]

