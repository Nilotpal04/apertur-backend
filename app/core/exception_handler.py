from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.user_exception import (
    EmailAlreadyExistsException,
    UsernameAlreadyExistsException
)

from app.exceptions.auth_exceptions import (
    InvalidCredentialsException
)
from pip._vendor.requests.api import request

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