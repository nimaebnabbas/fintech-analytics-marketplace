"""Subscription routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"]
)

@router.get("/packages")
async def get_packages(db: Session = Depends(get_db), language: str = "en"):
    """Get all subscription packages"""
    # TODO: Implement get packages
    return {"message": "Subscription packages endpoint", "packages": []}

@router.post("/")
async def subscribe(subscription_data: dict, db: Session = Depends(get_db)):
    """Create subscription"""
    # TODO: Implement subscription creation
    return {"message": "Create subscription endpoint"}

@router.get("/user/{user_id}")
async def get_user_subscription(user_id: str, db: Session = Depends(get_db)):
    """Get user subscription"""
    # TODO: Implement get user subscription
    return {"message": "Get user subscription endpoint"}
