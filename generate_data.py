"""
Generates synthetic JSON event logs using Faker.
Includes a controlled error rate to test schema validation.
"""
import json
import random
from faker import Faker

def generate_events(num_records: int = 1000, error_rate: float = 0.05) -> None:
    fake = Faker()
    events = []
    
    # Mix of realistic domains and local test environments
    tenant_ids = ["admin", "test", "sample", "demo", fake.domain_word()]
    valid_plans = ["free", "pro", "enterprise"]

    for i in range(num_records):
        is_error = random.random() < error_rate
        
        event = {
            "event_id": fake.uuid4(),
            "event_name": "user.signup",
            # Generate a timestamp within the last 30 days
            "timestamp": fake.date_time_between(start_date="-30d", end_date="now").isoformat() + "Z",
            "tenant_id": random.choice(tenant_ids),
            
            # Inject string instead of int for user_id on some errors
            "user_id": fake.user_name() if is_error and random.random() < 0.5 else fake.random_int(min=1000, max=99999),
            
            # Inject invalid 'premium' plan on other errors
            "plan_type": "premium" if is_error and random.random() >= 0.5 else random.choice(valid_plans),
            
            # Realistic referral sources (URL, search engine, or None)
            "referral_source": fake.url() if random.random() > 0.3 else None
        }
        events.append(event)

    output_path = "data/raw_events.json"
    with open(output_path, "w") as f:
        json.dump(events, f, indent=2)
        
    print(f"Generated {num_records} events in {output_path} (Approx {int(num_records * error_rate)} intentional errors)")

if __name__ == "__main__":
    generate_events(num_records=1000, error_rate=0.05)
