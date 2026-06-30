"""Product and Category models"""
from sqlalchemy import Column, String, Float, DateTime, Boolean, ForeignKey, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.database import Base
import enum

class MetalType(str, enum.Enum):
    GOLD = "gold"
    SILVER = "silver"
    PLATINUM = "platinum"
    PALLADIUM = "palladium"

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String(100), nullable=False, unique=True)
    name_fa = Column(String(100), nullable=False, unique=True)
    description_en = Column(Text)
    description_fa = Column(Text)
    metal_type = Column(Enum(MetalType), nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    products = relationship("Product", back_populates="category")
    
    def __repr__(self):
        return f"<Category(id={self.id}, metal_type={self.metal_type})>"

class Product(Base):
    __tablename__ = "products"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), nullable=False, index=True)
    name_en = Column(String(255), nullable=False)
    name_fa = Column(String(255), nullable=False)
    description_en = Column(Text)
    description_fa = Column(Text)
    
    # Pricing based on real-time data
    base_price_per_gram_usd = Column(Float, nullable=False)  # Updated from API
    base_price_per_gram_rial = Column(Float, nullable=False)
    current_price_usd = Column(Float)  # Real-time price
    current_price_rial = Column(Float)
    price_updated_at = Column(DateTime)
    
    # Product details
    purity_percentage = Column(Float)  # 99.9, 99.5, etc.
    weight_grams = Column(Float)  # Available weights
    metal_type = Column(Enum(MetalType), nullable=False, index=True)
    
    # Status
    is_available = Column(Boolean, default=True)
    stock_quantity = Column(Float, default=0)
    
    # SEO
    slug = Column(String(255), unique=True, index=True)
    meta_description_en = Column(String(160))
    meta_description_fa = Column(String(160))
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    
    def __repr__(self):
        return f"<Product(id={self.id}, name_en={self.name_en}, metal_type={self.metal_type})>"
