# test_sync.py

from pymongo import MongoClient
from app.core.config import settings

try:
    client = MongoClient(
        settings.mongodb_url,
        serverSelectionTimeoutMS=5000
    )

    print(client.admin.command("ping"))

except Exception as e:
    print(type(e).__name__)
    print(e)