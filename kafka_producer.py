
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

events = [
    {"user_id": 1, "product_id": 101, "event_type": "view", "timestamp": "2025-04-17T10:00:00Z"},
    {"user_id": 2, "product_id": 103, "event_type": "click", "timestamp": "2025-04-17T10:01:00Z"},
    {"user_id": 1, "product_id": 104, "event_type": "add_to_cart", "timestamp": "2025-04-17T10:02:00Z"}
]

for event in events:
    producer.send('clickstream_topic', event)
    print(f"Sent: {event}")
    time.sleep(1)

producer.flush()
