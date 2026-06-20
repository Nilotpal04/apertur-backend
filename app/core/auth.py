from datetime import datetime, timedelta, UTC
from jose import jwt, JWTError
from app.core.config import settings

def create_access_token(user_id: str) -> str:
    
    expire = datetime.now(UTC) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    
    payload = {
        "sub": user_id,
        "type": "access",
        "exp": expire
    }
    
    token = jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm
    )
    
    return token

def create_refresh_token(user_id: str) -> str:
    
    expire = datetime.now(UTC) + timedelta(
        minutes=settings.refresh_token_expire_days
    )
    
    payload = {
        "sub": user_id,
        "type": "refresh",
        "exp": expire
    }
    
    token = jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm
    )
    
    return token

def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.jwt_secret_key,
        algorithms=[settings.jwt_algorithm]
    )