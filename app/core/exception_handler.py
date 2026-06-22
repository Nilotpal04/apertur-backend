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
from pip._vendor.requests.api import request
from app.exceptions.post_exceptions import PostNotFoundException

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