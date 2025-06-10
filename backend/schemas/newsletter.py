from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class NewsletterBase(BaseModel):
    email: EmailStr
    is_active: bool = True

class NewsletterCreate(NewsletterBase):
    pass

class Newsletter(NewsletterBase):
    id: str
    created_at: datetime = datetime.utcnow()
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True 