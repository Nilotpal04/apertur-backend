from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.database import connect_to_mongodb
from app.routes.user import router as user_router
from app.routes.auth import router as auth_router
from app.routes.post import router as post_router

from app.core.exception_handler import (
    register_exception_handlers
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongodb()
    yield


app = FastAPI(lifespan=lifespan, title="Apertur API")

register_exception_handlers(app)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(post_router)