from fastapi import FastAPI
from routes.crypto import router as crypto_router

# Initialize FastAPI app
app = FastAPI()

# Include the routes from the routes module
app.include_router(crypto_router)
