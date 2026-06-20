from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.user_service import register_user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
async def register_user(user_data: UserCreate):
    return await register_user_service(user_data)
    
