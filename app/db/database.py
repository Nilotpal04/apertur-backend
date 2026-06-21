from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import certifi
from app.core.config import settings
from app.models.user import User
from app.models.post import Post

client = AsyncIOMotorClient(
    settings.mongodb_url,
    tls=True,
    tlsCAFile=certifi.where(),
    tlsAllowInvalidCertificates=False,
)


async def connect_to_mongodb():
    await init_beanie(
        database=client.apertur_db,
        document_models=[
            User,
            Post
        ]
    )

    print("Connected to MongoDB Atlas")