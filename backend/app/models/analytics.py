"""Analytics and Market Data models"""
from sqlalchemy import Column, String, Float, DateTime, Text, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from app.database import Base

class MarketData(Base):
    __tablename__ = "market_data"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    market_name = Column(String(100), nullable=False, index=True)  # e.g., 'Gold', 'Silver', 'Dollar', 'Oil'
    market_name_fa = Column(String(100))
    symbol = Column(String(50), nullable=False, index=True)  # e.g., 'XAU/USD', 'USD/IRR'
    language = Column(String(10), default="en")
    
    # Price Data
    current_price = Column(Float, nullable=False)
    previous_close = Column(Float)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    volume = Column(Float)
    
    # Change Metrics
    price_change = Column(Float)  # Absolute change
    price_change_percent = Column(Float)  # Percentage change
    
    # Timestamps (minute-level for precious metals, hourly for others)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    data_updated_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<MarketData(id={self.id}, symbol={self.symbol}, price={self.current_price})>"

class AnalyticsData(Base):
    __tablename__ = "analytics_data"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title_en = Column(String(255), nullable=False)
    title_fa = Column(String(255), nullable=False)
    
    # Analysis Content
    content_en = Column(Text, nullable=False)
    content_fa = Column(Text, nullable=False)
    summary_en = Column(Text)
    summary_fa = Column(Text)
    
    # Political Psychology Analysis
    political_leader_analysis = Column(JSON)  # {"leader_name": "...", "analysis": "...", "impact_level": "high/medium/low"}
    market_impact_score = Column(Float)  # 1-10 scale
    
    # Associated Markets
    affected_markets = Column(JSON)  # ["Gold", "Dollar", "Oil", ...]
    
    # Military/Conflict Context
    conflict_region = Column(String(255))
    severity_level = Column(String(50))  # "high", "medium", "low"
    
    # SEO
    slug = Column(String(255), unique=True, index=True)
    meta_description_en = Column(String(160))
    meta_description_fa = Column(String(160))
    keywords_en = Column(String(255))
    keywords_fa = Column(String(255))
    
    # Status
    is_published = Column(Integer, default=0)  # 0 = draft, 1 = published
    views_count = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = Column(DateTime)
    
    def __repr__(self):
        return f"<AnalyticsData(id={self.id}, title_en={self.title_en}, is_published={self.is_published})>"
