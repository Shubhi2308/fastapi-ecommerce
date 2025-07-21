# models.py
from pydantic import BaseModel, Field
from typing import List, Optional

class Size(BaseModel):
    size: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    sizes: Optional[List[Size]] = []

class OrderItem(BaseModel):
    productId: str = Field(..., min_length=1)
    qty: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    userId: str = Field(..., min_length=1)
    items: List[OrderItem]
