"""
Write a Python script which can generate 100 valid eReceiver
JSON Data Cloud Events with random combinations data.status,
data.type and data.hash values. Values must adhere to the
constraints described in the eReceiver Functional Specifications section Payload Validation.
"""
import uuid
import random
import hashlib
import json

# Define the constraints
VALID_STATUSES = ["complete", "incomplete", "cancelled"]
VALID_TYPES = [1, 2, 5, 11]

# Function to generate a valid MD5 hash
def generate_md5_hash():
    return hashlib.md5(uuid.uuid4().bytes).hexdigest()

# Generate 100 valid eReceiver JSON Data Cloud Events
events = []
for _ in range(100):
    event = {
        "specversion": "1.0",
        "type": "com.evertest.event",
        "source": "ereceiver",
        "subject": "DATA",
        "id": str(uuid.uuid4()),
        "time": "2024-01-01T12:01:01Z",
        "datacontenttype": "application/json",
        "data": {
            "status": random.choice(VALID_STATUSES),
            "type": random.choice(VALID_TYPES),
            "hash": generate_md5_hash()
        }
    }
    events.append(event)

# Print the generated events
for idx, event in enumerate(events, start=1):
    print(f"Event {idx}:")
    print(json.dumps(event, indent=4))
    print()

# Optionally, save events to a file
with open("generated_events.json", "w") as f:
    json.dump(events, f, indent=4)
    print(f"\nGenerated events saved to generated_events.json")
