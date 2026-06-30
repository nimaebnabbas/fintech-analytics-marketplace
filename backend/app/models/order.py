"""Order and OrderItem models"""
from sqlalchemy import Column, String, Float, DateTime, Boolean, ForeignKey, Integer, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.database import Base
import enum

class OrderStatus(str, enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

class PaymentStatus(str, enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class PaymentMethod(str, enum.Enum):
    ZARINPAL = "zarinpal"
    CRYPTO = "crypto"
    BANK_TRANSFER = "bank_transfer"

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    order_number = Column(String(50), unique=True, nullable=False, index=True)
    
    # Pricing
    subtotal_usd = Column(Float, nullable=False)
    subtotal_rial = Column(Float, nullable=False)
    tax_usd = Column(Float, default=0)
    tax_rial = Column(Float, default=0)
    shipping_cost_usd = Column(Float, default=0)
    shipping_cost_rial = Column(Float, default=0)
    total_usd = Column(Float, nullable=False)
    total_rial = Column(Float, nullable=False)
    currency = Column(String(10), nullable=False)  # 'USD' or 'RIAL'
    
    # Status
    order_status = Column(Enum(OrderStatus), default=OrderStatus.PENDING, index=True)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    payment_method = Column(Enum(PaymentMethod))
    
    # Payment Gateway References
    zarinpal_ref_id = Column(String(255))  # For Zarinpal
    crypto_tx_hash = Column(String(255))  # For Crypto
    
    # Delivery Info
    shipping_address = Column(Text)
    tracking_number = Column(String(100))
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    paid_at = Column(DateTime)
    shipped_at = Column(DateTime)
    delivered_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Order(id={self.id}, order_number={self.order_number}, status={self.order_status})>"

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.id"), nullable=False, index=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), nullable=False)
    
    # Quantity and Pricing
    quantity = Column(Float, nullable=False)  # In grams for metals
    unit_price_usd = Column(Float, nullable=False)
    unit_price_rial = Column(Float, nullable=False)
    total_price_usd = Column(Float, nullable=False)
    total_price_rial = Column(Float, nullable=False)
    
    # Price at time of order (for history)
    price_locked_at = Column(DateTime, default=datetime.utcnow)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
    
    def __repr__(self):
        return f"<OrderItem(id={self.id}, product_id={self.product_id}, quantity={self.quantity})>"
