import asyncio
from database.connection import Database
from dotenv import load_dotenv
import os

async def test_connection():
    try:
        await Database.connect_db()
        print("Successfully connected to MongoDB!")
        
        # Test database operations
        db = Database.get_db()
        result = await db.products.find_one()
        print("Database test query successful!")
        
        await Database.close_db()
        print("Connection closed successfully!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_connection()) 