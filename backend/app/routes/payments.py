"""Payment routes for Zarinpal and Crypto"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.payment import PaymentService
from app.models import Order
import os

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

payment_service = PaymentService()

@router.post("/zarinpal/create")
async def create_zarinpal_payment(order_id: str, amount_rial: float, db: Session = Depends(get_db)):
    """
    Create Zarinpal payment request
    Returns payment URL for user to complete payment
    """
    # Verify order exists and belongs to user
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    # Create payment
    payment_result = await payment_service.create_zarinpal_payment(
        amount_rial=amount_rial,
        order_id=order_id,
        description=f"Order {order.order_number}"
    )
    
    if not payment_result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create payment"
        )
    
    # Store authority in order
    order.zarinpal_ref_id = payment_result["authority"]
    db.commit()
    
    return payment_result

@router.get("/zarinpal/callback")
async def zarinpal_callback(
    authority: str = Query(...),
    status_param: str = Query(..., alias="status"),
    db: Session = Depends(get_db)
):
    """
    Zarinpal payment callback
    Called after user completes or cancels payment
    """
    if status_param != "OK":
        return {
            "success": False,
            "message": "Payment cancelled or failed"
        }
    
    # Find order by authority
    order = db.query(Order).filter(Order.zarinpal_ref_id == authority).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    # Verify payment
    ref_id = await payment_service.verify_zarinpal_payment(
        authority=authority,
        amount_rial=int(order.total_rial)
    )
    
    if ref_id:
        # Update order status
        order.payment_status = "completed"
        order.zarinpal_ref_id = ref_id
        db.commit()
        
        return {
            "success": True,
            "message": "Payment verified successfully",
            "ref_id": ref_id,
            "order_id": str(order.id)
        }
    else:
        return {
            "success": False,
            "message": "Payment verification failed"
        }

@router.post("/crypto/create")
async def create_crypto_payment(order_id: str, amount_usd: float, db: Session = Depends(get_db)):
    """
    Create Crypto payment request (Tether/USDT)
    TODO: Integrate with actual crypto payment provider
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    payment_result = await payment_service.create_crypto_payment(
        amount_usd=amount_usd,
        order_id=order_id
    )
    
    return payment_result

@router.get("/status/{order_id}")
async def get_payment_status(order_id: str, db: Session = Depends(get_db)):
    """
    Get payment status for an order
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    return {
        "order_id": str(order.id),
        "order_number": order.order_number,
        "payment_status": order.payment_status,
        "payment_method": order.payment_method,
        "amount_usd": order.total_usd,
        "amount_rial": order.total_rial
    }
