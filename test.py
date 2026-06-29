from motor.motor_asyncio import AsyncIOMotorClient
import certifi
import asyncio

client = AsyncIOMotorClient(
    "<your mongodb url>",
    tls=True,
    tlsCAFile=certifi.where()
)

async def test():
    await client.admin.command("ping")
    print("Connected!")

asyncio.run(test())