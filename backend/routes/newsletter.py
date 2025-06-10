from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId

from ..schemas.newsletter import Newsletter, NewsletterCreate
from ..database.connection import Database

router = APIRouter()

@router.get("/", response_model=List[Newsletter])
async def get_subscribers():
    subscribers = []
    cursor = Database.get_db().newsletter.find()
    async for document in cursor:
        document["id"] = str(document.pop("_id"))
        subscribers.append(Newsletter(**document))
    return subscribers

@router.post("/", response_model=Newsletter, status_code=status.HTTP_201_CREATED)
async def subscribe_newsletter(subscriber: NewsletterCreate):
    # Check if email already exists
    existing = await Database.get_db().newsletter.find_one({"email": subscriber.email})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already subscribed"
        )
    
    subscriber_dict = subscriber.model_dump()
    result = await Database.get_db().newsletter.insert_one(subscriber_dict)
    created_subscriber = await Database.get_db().newsletter.find_one({"_id": result.inserted_id})
    created_subscriber["id"] = str(created_subscriber.pop("_id"))
    return Newsletter(**created_subscriber) 