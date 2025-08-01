#!/usr/bin/env python3
"""
Bitcoin Price Prediction Service
Simple Bitcoin price prediction service that writes to shared file
"""

import os
import time
import json
import requests
import random
from datetime import datetime
from pathlib import Path

# Shared file path for Go service integration
SHARED_DIR = Path("/shared")
PREDICTION_FILE = SHARED_DIR / "prediction.json"

def get_current_price():
    """Get current Bitcoin price from Coinbase"""
    try:
        response = requests.get(
            "https://api.exchange.coinbase.com/products/BTC-USD/ticker",
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return float(data['price'])
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def generate_prediction(current_price):
    """Generate a simple price prediction"""
    # Simple prediction: current price +/- 0.5% to 2%
    change_percent = random.uniform(-2.0, 2.0)
    predicted_price = current_price * (1 + change_percent / 100)
    return predicted_price

def write_prediction():
    """Write prediction to shared file"""
    try:
        # Ensure shared directory exists
        SHARED_DIR.mkdir(exist_ok=True)

        # Get current price
        current_price = get_current_price()
        if not current_price:
            print("Could not fetch current price")
            return False

        # Generate prediction
        predicted_price = generate_prediction(current_price)

        # Create prediction data
        prediction_data = {
            "timestamp": datetime.now().isoformat(),
            "predicted_price": round(predicted_price, 2),
            "current_price": round(current_price, 2),
            "prediction_horizon": "5 minutes",
            "data_points": 100,
            "volume_24h": 0,
            "price_change_24h": 0
        }

        # Write to file
        with open(PREDICTION_FILE, 'w') as f:
            json.dump(prediction_data, f, indent=2)

        print(f"Prediction written: ${predicted_price:.2f} (current: ${current_price:.2f})")
        return True

    except Exception as e:
        print(f"Error writing prediction: {e}")
        return False

def main():
    """Main prediction loop"""
    print("Starting Bitcoin Prediction Service...")

    while True:
        try:
            success = write_prediction()
            if success:
                print("Prediction updated successfully")
            else:
                print("Failed to update prediction")

        except Exception as e:
            print(f"Error in main loop: {e}")

        # Wait 30 seconds before next prediction
        time.sleep(30)

if __name__ == "__main__":
    main()