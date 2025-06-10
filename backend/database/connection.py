from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
from fastapi import HTTPException

load_dotenv()

class Database:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect_db(cls):
        try:
            cls.client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
            # Verify connection
            await cls.client.admin.command('ping')
            cls.db = cls.client[os.getenv("DATABASE_NAME")]
            print("Connected to MongoDB!")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail="Could not connect to the database"
            )

    @classmethod
    async def close_db(cls):
        if cls.client is not None:
            cls.client.close()
            print("MongoDB connection closed.")

    @classmethod
    def get_db(cls):
        if cls.db is None:
            raise HTTPException(
                status_code=500,
                detail="Database not initialized"
            )
        return cls.db 