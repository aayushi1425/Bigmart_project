from pydantic import BaseModel
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    description: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: str
    created_at: datetime = datetime.utcnow()

    class Config:
        from_attributes = True 