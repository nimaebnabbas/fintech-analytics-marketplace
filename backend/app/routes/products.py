"""Product routes"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/")
async def get_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 20):
    """Get all products with pagination"""
    # TODO: Implement product listing
    return {"message": "Products listing endpoint", "products": []}

@router.get("/{product_id}")
async def get_product(product_id: str, db: Session = Depends(get_db)):
    """Get single product"""
    # TODO: Implement get single product
    return {"message": "Get single product endpoint"}

@router.get("/category/{category_id}")
async def get_products_by_category(category_id: str, db: Session = Depends(get_db)):
    """Get products by category"""
    # TODO: Implement filter by category
    return {"message": "Get products by category endpoint"}
