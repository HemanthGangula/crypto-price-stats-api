import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
DB_NAME = "crypto_db"
COLLECTION_NAME = "crypto_snapshots"