from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI(title="Fraud Detection API")

model, scaler = joblib.load("models/isolation_forest.pkl")

class Transaction(BaseModel):
    amount: float
    hour: int
    day_of_week: int
    distance_from_home: float

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")

@app.post("/predict")
def predict(tx: Transaction):
    data = np.array([[ 
        tx.amount,
        tx.hour,
        tx.day_of_week,
        tx.distance_from_home
    ]])

    data_scaled = scaler.transform(data)
    score = model.decision_function(data_scaled)[0]

# Convert anomaly score to risk (higher = more risky)
    raw_risk = -score

# Non-linear amplification (business-sensitive)
    fraud_risk_score = min(raw_risk * 5, 1.0)

# Business threshold (false negatives are costly)
    risk_level = "HIGH" if fraud_risk_score >= 0.3 else "LOW"

    return {
        "fraud_risk_score": round(fraud_risk_score, 3),
        "risk_level": risk_level,
        "reasoning": (
        "Transaction shows unusual patterns in amount, timing, "
        "and distance compared to normal behavior"
    )
}

