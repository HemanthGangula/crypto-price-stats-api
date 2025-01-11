from fastapi import APIRouter
from models.coin import CryptoSnapshot
from services.database import get_snapshot, get_all_snapshots
from typing import List

router = APIRouter()

@router.get("/crypto/{coin_id}", response_model=CryptoSnapshot)
def get_latest_snapshot(coin_id: str):
    snapshot = get_snapshot(coin_id)
    if snapshot:
        return CryptoSnapshot(
            coin_id=snapshot["coin_id"],
            current_price=snapshot["current_price"],
            market_cap=snapshot["market_cap"],
            price_change_percentage_24h=snapshot["price_change_percentage_24h"],
            timestamp=snapshot["timestamp"].isoformat(),
        )
    return {"error": "Coin not found"}

@router.get("/crypto/history/{coin_id}", response_model=List[CryptoSnapshot])
def get_all_snapshots_route(coin_id: str):
    snapshots = get_all_snapshots(coin_id)
    return [
        CryptoSnapshot(
            coin_id=snapshot["coin_id"],
            current_price=snapshot["current_price"],
            market_cap=snapshot["market_cap"],
            price_change_percentage_24h=snapshot["price_change_percentage_24h"],
            timestamp=snapshot["timestamp"].isoformat(),
        )
        for snapshot in snapshots
    ]
