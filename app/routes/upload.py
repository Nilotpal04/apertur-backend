from fastapi import (
    APIRouter,
    UploadFile,
    File
)
from app.dependencies.auth import CurrentUser

from app.services.upload_service import (
    upload_image_service
)

router = APIRouter(
    prefix="/uploads",
    tags=["Uploads"]
)

@router.post("/image")
async def upload_image(
    file: UploadFile = File(...),
    current_user: CurrentUser = None
):
    return await upload_image_service(
        file
    )