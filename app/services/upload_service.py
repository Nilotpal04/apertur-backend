import cloudinary.uploader
from fastapi import UploadFile
from app.exceptions.upload_exceptions import (
    InvalidImageException,
    ImageUploadFailedException
)

allowed_types = [
    "image/jpeg",
    "image/png",
    "image/webp"
]

async def upload_image_service(file: UploadFile):
    if file.content_type not in allowed_types:
        raise InvalidImageException()
    try:
        result = cloudinary.uploader.upload(
            file.file,
            folder="apertur"
        )
    except Exception:
        raise ImageUploadFailedException()
    return {
        "url": result["secure_url"]
    }