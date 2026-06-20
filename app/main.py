from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import connect_to_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongodb()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Welcome to Apertur API"}