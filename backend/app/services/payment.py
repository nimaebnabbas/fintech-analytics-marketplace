"""Payment processing service"""
import os
import requests
from typing import Optional, Dict
from enum import Enum

class PaymentProvider(Enum):
    ZARINPAL = "zarinpal"
    CRYPTO = "crypto"

class PaymentService:
    """Handle payment processing"""
    
    def __init__(self):
        self.zarinpal_merchant_id = os.getenv("ZARINPAL_MERCHANT_ID")
        self.zarinpal_api_url = "https://api.zarinpal.com/pg/v4/payment"
        self.crypto_api_key = os.getenv("CRYPTO_API_KEY")
    
    async def create_zarinpal_payment(self, amount_rial: float, order_id: str, description: str) -> Optional[Dict]:
        """
        Create Zarinpal payment request (Rial)
        Returns payment URL
        """
        try:
            payload = {
                "merchant_id": self.zarinpal_merchant_id,
                "amount": int(amount_rial),
                "callback_url": f"{os.getenv('FRONTEND_URL')}/payment/callback",
                "description": description,
                "metadata": {
                    "order_id": order_id
                }
            }
            
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                f"{self.zarinpal_api_url}/request.json",
                json=payload,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("data", {}).get("authority"):
                    return {
                        "authority": data["data"]["authority"],
                        "payment_url": f"https://www.zarinpal.com/pg/StartPay/{data['data']['authority']}"
                    }
            return None
        except Exception as e:
            print(f"Zarinpal error: {str(e)}")
            return None
    
    async def verify_zarinpal_payment(self, authority: str, amount_rial: int) -> Optional[str]:
        """
        Verify Zarinpal payment
        Returns transaction reference ID if successful
        """
        try:
            payload = {
                "merchant_id": self.zarinpal_merchant_id,
                "authority": authority,
                "amount": amount_rial
            }
            
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                f"{self.zarinpal_api_url}/verify.json",
                json=payload,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("data", {}).get("ref_id"):
                    return data["data"]["ref_id"]
            return None
        except Exception as e:
            print(f"Zarinpal verification error: {str(e)}")
            return None
    
    async def create_crypto_payment(self, amount_usd: float, order_id: str) -> Optional[Dict]:
        """
        Create Crypto payment request (Tether/USDT)
        TODO: Implement with actual crypto payment provider
        """
        # Placeholder for crypto integration
        return {
            "payment_address": "0x...",
            "amount_usdt": amount_usd,
            "order_id": order_id
        }
