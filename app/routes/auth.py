from fastapi import APIRouter
from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

from app.services.auth_service import login_user_service
from app.routes.user import router

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login", response_model=TokenResponse)
async def login_user(login_data: LoginRequest):
    return await login_user_service(login_data)
        