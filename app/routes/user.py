from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import register_user_service
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