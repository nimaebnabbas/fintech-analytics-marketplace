"""Subscription schemas"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class SubscriptionPackageResponse(BaseModel):
    id: str
    name_en: str
    name_fa: str
    price_usd: float
    price_rial: float
    tier_level: int
    features_en: Optional[str]
    features_fa: Optional[str]
    is_active: bool
    
    class Config:
        from_attributes = True

class SubscriptionCreate(BaseModel):
    package_id: str
    currency: str  # 'USD' or 'RIAL'

class SubscriptionResponse(BaseModel):
    id: str
    user_id: str
    package: SubscriptionPackageResponse
    currency: str
    is_active: bool
    start_date: datetime
    end_date: Optional[datetime]
    renewal_date: Optional[datetime]
    
    class Config:
        from_attributes = True
