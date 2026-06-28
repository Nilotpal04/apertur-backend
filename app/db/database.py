from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import certifi
from app.core.config import settings
from app.models.user import User
from app.models.post import Post
from app.models.like import Like
from app.models.follow import Follow
from app.models.frame import Frame
from app.models.notification import Notification

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
            Post,
            Like,
            Follow,
            Frame,
            Notification
        ]
    )

    print("Connected to MongoDB Atlas")