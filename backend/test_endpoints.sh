#!/bin/bash

# Define the endpoints to test
endpoints=(
  "/crypto/bitcoin"
  "/crypto/ethereum"
  "/crypto/matic-network"
  "/crypto/history/bitcoin"
  "/crypto/history/ethereum"
  "/crypto/history/matic-network"
)

# Loop through each endpoint and check the HTTP status code
for endpoint in "${endpoints[@]}"; do
  status=$(curl -o /dev/null -s -w "%{http_code}" http://127.0.0.1:8000"$endpoint")
  
  if [ "$status" -eq 200 ]; then
    echo "✔ $endpoint returned 200"
  else
    echo "✗ $endpoint returned $status"
  fi
done