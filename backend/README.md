# Cryptocurrency Tracker Backend

## Overview
This project fetches cryptocurrency data using the CoinGecko API and provides APIs for stats and calculations.

## Setup Instructions
1. Run `source venv/bin/activate` to activate the virtual environment.
2. Run `python src/app.py` to start the server.

## Dependencies
- Flask: Backend framework.
- Requests: To interact with CoinGecko API.
- PyMongo: To connect to MongoDB.
- Schedule: To schedule background jobs.


Data is stored in MongoDB. To run MongoDB in a Docker container, use the following command:
```bash
docker run -d --name mongodb -p 27017:27017 mongo
```

## Run the coin Fetcher code in /services/coin_fetcher.py
```bash
python3 services/coin_fetcher.py
```
so the data will be fetched and stored in the MongoDB.

#### Supported coins
- Bitcoin
- Ethereum
- Matic Network

### Run the server
```bash
uvicorn app:app --reload
```
from /backend directory

### Testing commands
```bash
curl http://127.0.0.1:8000/crypto/bitcoin
curl http://127.0.0.1:8000/crypto/ethereum
curl http://127.0.0.1:8000/crypto/matic-network

curl http://127.0.0.1:8000/crypto/history/bitcoin
curl http://127.0.0.1:8000/crypto/history/ethereum
curl http://127.0.0.1:8000/crypto/history/matic-network

curl "http://127.0.0.1:8000/deviation?coin=bitcoin"
curl "http://127.0.0.1:8000/deviation?coin=ethereum"
curl "http://127.0.0.1:8000/deviation?coin=matic-network"

```
