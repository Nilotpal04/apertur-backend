from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register")
async def register_user(user_data: UserCreate):

    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=user_data.password
    )

    await user.insert()

    return {
        "message": "User created successfully"
    }
    
