from fastapi import APIRouter
from app.schemas.auth import (
    LoginRequest,
    TokenResponse,
    RefreshTokenRequest
)

from app.services.auth_service import login_user_service, refresh_token_service
from app.routes.user import router

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login", response_model=TokenResponse)
async def login_user(login_data: LoginRequest):
    return await login_user_service(login_data)

@router.post("/refresh")
async def refresh_token(token_data: RefreshTokenRequest):
    return await refresh_token_service(
        token_data.refresh_token
    )