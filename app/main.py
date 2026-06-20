from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import connect_to_mongodb
from app.routes.user import router as user_router

from app.core.exception_handler import (
    register_exception_handlers
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongodb()
    yield


app = FastAPI(lifespan=lifespan)

register_exception_handlers(app)

app.include_router(user_router)