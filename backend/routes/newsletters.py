from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId

from schemas.newsletter import Newsletter, NewsletterCreate
from database.connection import Database

router = APIRouter()

@router.get("/", response_model=List[Newsletter])
async def get_newsletters():
    newsletters = []
    cursor = Database.get_db().newsletters.find()
    async for document in cursor:
        document["id"] = str(document.pop("_id"))
        newsletters.append(Newsletter(**document))
    return newsletters

@router.post("/", response_model=Newsletter, status_code=status.HTTP_201_CREATED)
async def create_newsletter(newsletter: NewsletterCreate):
    newsletter_dict = newsletter.model_dump()
    result = await Database.get_db().newsletters.insert_one(newsletter_dict)
    created_newsletter = await Database.get_db().newsletters.find_one({"_id": result.inserted_id})
    created_newsletter["id"] = str(created_newsletter.pop("_id"))
    return Newsletter(**created_newsletter) 