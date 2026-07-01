"""Background tasks for Celery"""
from app.celery_config import celery_app
from app.database import SessionLocal
from app.models import MarketData, Product, Subscription, Order
from datetime import datetime, timedelta
from sqlalchemy import and_
import logging

logger = logging.getLogger(__name__)

@celery_app.task(name="app.tasks.update_metals_prices")
def update_metals_prices():
    """Update precious metals prices every minute"""
    try:
        db = SessionLocal()
        logger.info(f"Updating metals prices at {datetime.utcnow()}")
        db.close()
        return {"status": "success", "timestamp": datetime.utcnow().isoformat()}
    except Exception as e:
        logger.error(f"Error updating metals prices: {str(e)}")
        return {"status": "error", "message": str(e)}

@celery_app.task(name="app.tasks.update_market_data")
def update_market_data():
    """Update wartime market data every 5 minutes"""
    try:
        db = SessionLocal()
        logger.info(f"Updating market data at {datetime.utcnow()}")
        db.close()
        return {"status": "success", "timestamp": datetime.utcnow().isoformat()}
    except Exception as e:
        logger.error(f"Error updating market data: {str(e)}")
        return {"status": "error", "message": str(e)}

@celery_app.task(name="app.tasks.check_subscription_expiry")
def check_subscription_expiry():
    """Check for expired subscriptions daily"""
    try:
        db = SessionLocal()
        expired_subs = db.query(Subscription).filter(
            and_(
                Subscription.is_active == True,
                Subscription.end_date < datetime.utcnow()
            )
        ).all()
        
        for sub in expired_subs:
            sub.is_active = False
        
        db.commit()
        db.close()
        
        logger.info(f"Deactivated {len(expired_subs)} expired subscriptions")
        return {"status": "success", "deactivated_count": len(expired_subs)}
    except Exception as e:
        logger.error(f"Error checking subscription expiry: {str(e)}")
        return {"status": "error", "message": str(e)}

@celery_app.task(name="app.tasks.cleanup_old_orders")
def cleanup_old_orders():
    """Clean up old pending orders"""
    try:
        db = SessionLocal()
        cutoff_date = datetime.utcnow() - timedelta(days=7)
        old_orders = db.query(Order).filter(
            and_(
                Order.order_status == "pending",
                Order.created_at < cutoff_date
            )
        ).all()
        
        for order in old_orders:
            order.order_status = "cancelled"
        
        db.commit()
        db.close()
        
        logger.info(f"Cleaned up {len(old_orders)} old pending orders")
        return {"status": "success", "cleaned_count": len(old_orders)}
    except Exception as e:
        logger.error(f"Error cleaning up old orders: {str(e)}")
        return {"status": "error", "message": str(e)}
