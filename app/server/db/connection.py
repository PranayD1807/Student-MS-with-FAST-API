import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URL")
if not MONGO_URI:
    raise ValueError("MONGODB_URL environment variable is missing")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client.prod
