from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def get_snapshot(coin_id: str):
    return collection.find_one({"coin_id": coin_id}, sort=[("timestamp", -1)])

def get_all_snapshots(coin_id: str):
    return collection.find({"coin_id": coin_id}).sort("timestamp", -1)
