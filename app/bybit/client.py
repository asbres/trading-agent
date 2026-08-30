import requests

from app.bybit.parser import BybitParser
from app.models.candle import Candle


class BybitClient:
    BASE_URL = "https://api.bybit.com"

    def __init__(self):
        self.session = requests.Session()

    def get_klines(
            self,
            symbol: str,
            interval: str,
            limit: int,
            category: str,
        ) -> list[Candle]:
            params = {
                "category": category,
                "symbol": symbol,
                "interval": interval,
                "limit": limit,
            }
    
            response = self.session.get(
                f"{self.BASE_URL}/v5/market/kline",
                params=params,
            )
    
            response.raise_for_status()
    
            data = response.json()
    
            return BybitParser.parse_candles(
                data["result"]["list"]
            )