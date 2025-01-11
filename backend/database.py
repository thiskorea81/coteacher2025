# backend/database.py
import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client["coteacher2025_db"]
