"""Celery configuration for background tasks"""
from celery import Celery
from celery.schedules import crontab
import os
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "fintech_tasks",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,
)

celery_app.conf.beat_schedule = {
    'update-precious-metals-prices': {
        'task': 'app.tasks.update_metals_prices',
        'schedule': crontab(minute='*'),
    },
    'update-market-data': {
        'task': 'app.tasks.update_market_data',
        'schedule': crontab(minute='*/5'),
    },
    'check-subscription-expiry': {
        'task': 'app.tasks.check_subscription_expiry',
        'schedule': crontab(hour='0', minute='0'),
    },
    'cleanup-old-orders': {
        'task': 'app.tasks.cleanup_old_orders',
        'schedule': crontab(hour='2', minute='0'),
    },
}
