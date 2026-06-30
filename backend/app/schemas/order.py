"""Order schemas"""
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItemCreate(BaseModel):
    product_id: str
    quantity: float  # In grams

class OrderCreate(BaseModel):
    items: List[OrderItemCreate]
    currency: str  # 'USD' or 'RIAL'
    shipping_address: str

class OrderResponse(BaseModel):
    id: str
    order_number: str
    total_usd: float
    total_rial: float
    currency: str
    order_status: str
    payment_status: str
    payment_method: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

class OrderDetailResponse(OrderResponse):
    subtotal_usd: float
    tax_usd: float
    shipping_cost_usd: float
    items: List
