from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId

from schemas.category import Category, CategoryCreate
from database.connection import Database

router = APIRouter()

@router.get("/", response_model=List[Category])
async def get_categories():
    categories = []
    cursor = Database.get_db().categories.find()
    async for document in cursor:
        document["id"] = str(document.pop("_id"))
        categories.append(Category(**document))
    return categories

@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreate):
    category_dict = category.model_dump()
    result = await Database.get_db().categories.insert_one(category_dict)
    created_category = await Database.get_db().categories.find_one({"_id": result.inserted_id})
    created_category["id"] = str(created_category.pop("_id"))
    return Category(**created_category) 