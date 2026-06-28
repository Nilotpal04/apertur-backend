from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.user_exception import (
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException,
    UserNotFoundException
)

from app.exceptions.post_exceptions import (
    PostNotFoundException,
    PostOwnershipException
)

from app.exceptions.auth_exceptions import (
    InvalidCredentialsException
)

from app.exceptions.upload_exceptions import (
    InvalidImageException,
    ImageUploadFailedException
)

from app.exceptions.post_exceptions import PostNotFoundException
from app.exceptions.notification_exceptions import NotificationNotFoundException

def register_exception_handlers(app: FastAPI):

    @app.exception_handler(EmailAlreadyExistsException)
    async def email_exists_handler(
        request: Request,
        exc: EmailAlreadyExistsException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "detail": "Email already registered"
            }
        )

    @app.exception_handler(UsernameAlreadyExistsException)
    async def username_exists_handler(
        request: Request,
        exc: UsernameAlreadyExistsException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "detail": "Username already registered"
            }
        )
        
    @app.exception_handler(
        InvalidCredentialsException
    )
    async def invalid_credentials_handler(
        request: Request,
        exc: InvalidCredentialsException
    ):
        return JSONResponse(
            status_code=401,
            content={
                "detail": "Invalid credentials"
            }
        )
    
    @app.exception_handler(
        UserNotFoundException
    )
    async def user_not_found_handler(
        request: Request,
        exc: UserNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": "User not found"
            }
        )
    
    @app.exception_handler(PostNotFoundException)
    async def post_not_found_handler(
        request: Request,
        exc: PostNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": "Post not found"
            }
        )
        
    @app.exception_handler(PostOwnershipException)
    async def post_ownership_exception_handler(
        request: Request,
        exc: PostOwnershipException
    ):
        return JSONResponse(
            status_code=403,
            content= {
                "detail": "You do not own this post"
            }
        )
    
    @app.exception_handler(InvalidImageException)
    async def invalid_image_exception_handler(
        request: Request,
        exc: InvalidImageException
    ):
        return JSONResponse(
            status_code=400,
            content= {
                "detail": "Invalid image type"
            }
        )
    
    @app.exception_handler(ImageUploadFailedException)
    async def image_upload_failed_exception_handler(
        request: Request,
        exc: ImageUploadFailedException
    ):
        return JSONResponse(
            status_code=500,
            content= {
                "detail": "Image upload failed"
            }
        )
    
    @app.exception_handler(NotificationNotFoundException)
    async def notification_not_found_exception_handler(
        request: Request,
        exc: NotificationNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content= {
                "detail": "Notification not found"
            }
        )