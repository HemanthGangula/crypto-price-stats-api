import requests
from pymongo import MongoClient
from datetime import datetime, timezone

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["crypto_db"]
collection = db["crypto_snapshots"]

# CoinGecko API
COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"
COINS = ["bitcoin", "ethereum", "matic-network"]
PARAMS = {
    "vs_currency": "usd",
    "ids": ",".join(COINS),
}

def fetch_and_store():
    try:
        print("Fetching cryptocurrency data...")
        response = requests.get(COINGECKO_URL, params=PARAMS)
        response.raise_for_status()
        data = response.json()

        for coin in data:
            snapshot = {
                "coin_id": coin["id"],
                "current_price": coin["current_price"],
                "market_cap": coin["market_cap"],
                "price_change_percentage_24h": coin["price_change_percentage_24h"],
                "timestamp": datetime.now(timezone.utc),
            }
            collection.insert_one(snapshot)
            print(f"Inserted data for {coin['id']}: {snapshot}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    fetch_and_store()
