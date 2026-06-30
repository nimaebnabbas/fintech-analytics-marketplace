"""Subscription models"""
from sqlalchemy import Column, String, Float, DateTime, Boolean, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.database import Base

class SubscriptionPackage(Base):
    __tablename__ = "subscription_packages"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name_en = Column(String(100), nullable=False)
    name_fa = Column(String(100), nullable=False)
    description_en = Column(Text)
    description_fa = Column(Text)
    price_usd = Column(Float, nullable=False)  # $10, $30, $50, $75, $100
    price_rial = Column(Float, nullable=False)  # 5M, 8M, 11M, 13M, 15M
    tier_level = Column(Integer, nullable=False)  # 1, 2, 3, 4, 5
    features_en = Column(Text)  # JSON or comma-separated
    features_fa = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    subscriptions = relationship("Subscription", back_populates="package")
    
    def __repr__(self):
        return f"<SubscriptionPackage(id={self.id}, name_en={self.name_en}, price_usd={self.price_usd})>"

class Subscription(Base):
    __tablename__ = "subscriptions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    package_id = Column(UUID(as_uuid=True), ForeignKey("subscription_packages.id"), nullable=False)
    currency = Column(String(10))  # 'USD' or 'RIAL'
    is_active = Column(Boolean, default=True)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime)
    renewal_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    package = relationship("SubscriptionPackage", back_populates="subscriptions")
    
    def __repr__(self):
        return f"<Subscription(id={self.id}, user_id={self.user_id}, package_id={self.package_id})>"
