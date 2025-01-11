from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from services.database import get_all_snapshots
import statistics

router = APIRouter()

class DeviationResponse(BaseModel):
    deviation: float

ALLOWED_COINS = {"bitcoin", "ethereum", "matic-network"}

@router.get("/deviation", response_model=DeviationResponse)
def get_deviation(coin: str = Query(..., description="Coin ID (bitcoin, ethereum, matic-network)")):
    if coin not in ALLOWED_COINS:
        raise HTTPException(status_code=400, detail=f"Coin '{coin}' is not supported.")

    snapshots_cursor = get_all_snapshots(coin).limit(100)
    prices = [snapshot["current_price"] for snapshot in snapshots_cursor]

    if not prices:
        raise HTTPException(status_code=404, detail=f"No data found for coin '{coin}'.")

    if len(prices) < 2:
        deviation = 0.0
    else:
        deviation = statistics.pstdev(prices)

    return {"deviation": round(deviation, 2)}