from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    title: str
    description: str
    price: float
    rating: float = Field(ge=0, le=5)
    image: str
    category: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    rating: Optional[float] = Field(None, ge=0, le=5)
    image: Optional[str] = None
    category: Optional[str] = None

class Product(ProductBase):
    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True 