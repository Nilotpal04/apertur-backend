from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import connect_to_mongodb
from app.routes.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongodb()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Apertur API"}