import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

N = 100_000
FRAUD_RATE = 0.02

data = []
start = datetime(2025, 1, 1)

for i in range(N):
    is_fraud = 1 if random.random() < FRAUD_RATE else 0
    ts = start + timedelta(minutes=random.randint(0, 60*24*180))

    if is_fraud:
        amount = random.uniform(20000, 200000)
        distance = random.uniform(50, 500)
        hour = random.randint(0, 5)
        fraud_type = random.choice(["card_cloning", "account_takeover"])
    else:
        amount = random.uniform(100, 5000)
        distance = random.uniform(0, 15)
        hour = random.randint(8, 22)
        fraud_type = "none"

    data.append({
        "transaction_id": f"TXN_{i:08d}",
        "customer_id": f"CUST_{random.randint(1,5000):05d}",
        "card_number": f"CARD_{random.randint(10000,99999)}",
        "timestamp": ts.isoformat(),
        "amount": round(amount,2),
        "merchant_id": f"MERCHANT_{random.randint(1000,9999)}",
        "merchant_category": random.choice(
            ["grocery","electronics","gas","restaurant","retail","jewelry","luxury_goods"]
        ),
        "merchant_lat": round(random.uniform(8,37),4),
        "merchant_long": round(random.uniform(68,97),4),
        "is_fraud": is_fraud,
        "fraud_type": fraud_type,
        "hour": hour,
        "day_of_week": ts.weekday(),
        "month": ts.month,
        "distance_from_home": round(distance,2)
    })

df = pd.DataFrame(data)
df.to_csv("data/transactions.csv", index=False)

print("Dataset generated")

