import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(var_name, default=None):
    value = os.getenv(var_name, default)
    if value is None:
        raise EnvironmentError(f"Environment variable {var_name} is not set.")
    return value

# For Development
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
DB_NAME = "crypto_db"
COLLECTION_NAME = "crypto_snapshots"


# For Production
"""

try:
    MONGO_USERNAME = get_env_variable("MONGO_USERNAME")
    MONGO_PASSWORD = get_env_variable("MONGO_PASSWORD")
    MONGO_CLUSTER = get_env_variable("MONGO_CLUSTER")

    MONGO_URI = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/?retryWrites=true&w=majority"
    DB_NAME = "crypto_db"
    COLLECTION_NAME = "crypto_snapshots"
except EnvironmentError as e:
    print(f"Configuration error: {e}")
    MONGO_URI = None
    DB_NAME = None
    COLLECTION_NAME = None

"""