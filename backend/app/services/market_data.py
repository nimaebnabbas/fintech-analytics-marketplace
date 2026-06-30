"""Market data service for real-time prices"""
import os
import aiohttp
from typing import Optional, Dict, List
from datetime import datetime

class MarketDataService:
    """Fetch real-time market data"""
    
    def __init__(self):
        self.metals_api_key = os.getenv("METALS_API_KEY")
        self.finnhub_api_key = os.getenv("FINNHUB_API_KEY")
        self.metals_api_url = "https://api.metals.live/v1/spot"
        self.finnhub_url = "https://finnhub.io/api/v1"
    
    async def get_precious_metals_prices(self) -> Optional[Dict]:
        """
        Get real-time precious metals prices (Gold, Silver, Platinum)
        Updates every minute
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.metals_api_url) as response:
                    if response.status == 200:
                        data = await response.json()
                        return {
                            "gold_usd": data.get("gold"),
                            "silver_usd": data.get("silver"),
                            "platinum_usd": data.get("platinum"),
                            "palladium_usd": data.get("palladium"),
                            "timestamp": datetime.utcnow().isoformat()
                        }
        except Exception as e:
            print(f"Metals API error: {str(e)}")
            return None
    
    async def get_wartime_market_data(self) -> Optional[Dict]:
        """
        Get market data for wartime scenarios
        Oil, currencies, indices affected by geopolitical tensions
        """
        try:
            # Using Finnhub for broader market data
            symbols = ["USOIL", "EURUSD", "GBPUSD", "^GSPC"]
            data = {}
            
            async with aiohttp.ClientSession() as session:
                for symbol in symbols:
                    url = f"{self.finnhub_url}/quote?symbol={symbol}&token={self.finnhub_api_key}"
                    async with session.get(url) as response:
                        if response.status == 200:
                            quote = await response.json()
                            data[symbol] = {
                                "price": quote.get("c"),
                                "change": quote.get("d"),
                                "change_percent": quote.get("dp"),
                                "high": quote.get("h"),
                                "low": quote.get("l"),
                                "open": quote.get("o"),
                                "volume": quote.get("v")
                            }
            
            return data
        except Exception as e:
            print(f"Finnhub API error: {str(e)}")
            return None
    
    async def convert_usd_to_rial(self, amount_usd: float) -> Optional[float]:
        """
        Convert USD to IRR using real-time exchange rate
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.finnhub_url}/quote?symbol=USDIRR&token={self.finnhub_api_key}"
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        exchange_rate = data.get("c")  # Current price
                        return amount_usd * exchange_rate
        except Exception as e:
            print(f"Exchange rate error: {str(e)}")
            return None
