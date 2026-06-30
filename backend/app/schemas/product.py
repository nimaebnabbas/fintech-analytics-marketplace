"""Product schemas"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoryResponse(BaseModel):
    id: str
    name_en: str
    name_fa: str
    metal_type: str
    
    class Config:
        from_attributes = True

class ProductResponse(BaseModel):
    id: str
    category: CategoryResponse
    name_en: str
    name_fa: str
    current_price_usd: Optional[float]
    current_price_rial: Optional[float]
    purity_percentage: float
    weight_grams: float
    metal_type: str
    is_available: bool
    stock_quantity: float
    slug: str
    
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    category_id: str
    name_en: str
    name_fa: str
    description_en: Optional[str]
    description_fa: Optional[str]
    purity_percentage: float
    weight_grams: float
    metal_type: str
