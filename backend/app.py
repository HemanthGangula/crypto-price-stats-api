from fastapi import FastAPI
from routes.crypto import router as crypto_router
from routes.deviation import router as deviation_router  # Import the deviation router

# Initialize FastAPI app
app = FastAPI()

# Include the routers
app.include_router(crypto_router)
app.include_router(deviation_router)  # Include the deviation router

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)