from pydantic import BaseModel

class CryptoSnapshot(BaseModel):
    coin_id: str
    current_price: float
    market_cap: int
    price_change_percentage_24h: float
    timestamp: str
