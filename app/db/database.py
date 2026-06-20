from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings


client = AsyncIOMotorClient(settings.mongodb_url)


async def connect_to_mongodb():
    await client.admin.command("ping")
    print("Connected to MongoDB Atlas")