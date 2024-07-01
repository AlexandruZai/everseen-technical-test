"""
Using Python, write a script to send valid and invalid POST requests
to the eReceiver service endpoint.
Include checks for expected responses and error logs.
"""

import requests
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='/var/log/ereceiver-service.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s: [ eReceiver ] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Define the base URL of the eReceiver service
BASE_URL = 'http://localhost:5000/api/v1/data'

# Function to send HTTP POST request with payload
def send_post_request(payload):
    try:
        response = requests.post(BASE_URL, json=payload)
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP POST request failed: {e}")
        return None

# Function to send a valid payload
def send_valid_payload():
    valid_payload = {
        "status": "complete",
        "type": 1,
        "hash": "661f8009fa8e56a9d0e94a0a644397d7"
    }
    response = send_post_request(valid_payload)
    if response:
        print(f"Valid payload sent successfully. Response status code: {response.status_code}")
    else:
        print("Failed to send valid payload.")

# Function to send an invalid payload
def send_invalid_payload():
    invalid_payload = {
        "status": None,  # Invalid: status cannot be None
        "type": 1,
        "hash": "661f8009fa8e56a9d0e94a0a644397d7"
    }
    response = send_post_request(invalid_payload)
    if response:
        print(f"Invalid payload sent successfully. Response status code: {response.status_code}")
    else:
        print("Failed to send invalid payload.")

# Example usage
if __name__ == "__main__":
    send_valid_payload()
    send_invalid_payload()
