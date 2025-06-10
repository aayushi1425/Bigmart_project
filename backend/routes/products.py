from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from datetime import datetime

from schemas.product import Product, ProductCreate, ProductUpdate
from database.connection import Database

router = APIRouter()

@router.get("/", response_model=List[Product])
async def get_products():
    products = []
    cursor = Database.get_db().products.find()
    async for document in cursor:
        document["id"] = str(document.pop("_id"))
        products.append(Product(**document))
    return products

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")
    
    product = await Database.get_db().products.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product["id"] = str(product.pop("_id"))
    return Product(**product)

@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    product_dict = product.model_dump()
    product_dict["created_at"] = datetime.utcnow()
    product_dict["updated_at"] = datetime.utcnow()
    
    result = await Database.get_db().products.insert_one(product_dict)
    created_product = await Database.get_db().products.find_one({"_id": result.inserted_id})
    created_product["id"] = str(created_product.pop("_id"))
    return Product(**created_product)

@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: str, product: ProductUpdate):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")
    
    update_data = product.model_dump(exclude_unset=True)
    if update_data:
        update_data["updated_at"] = datetime.utcnow()
        result = await Database.get_db().products.update_one(
            {"_id": ObjectId(product_id)},
            {"$set": update_data}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Product not found")
    
    updated_product = await Database.get_db().products.find_one({"_id": ObjectId(product_id)})
    updated_product["id"] = str(updated_product.pop("_id"))
    return Product(**updated_product)

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID")
    
    result = await Database.get_db().products.delete_one({"_id": ObjectId(product_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found") 