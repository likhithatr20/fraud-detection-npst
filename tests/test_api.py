from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_predict():
    res = client.post("/predict", json={
        "amount": 90000,
        "hour": 2,
        "day_of_week": 6,
        "distance_from_home": 120
    })
    assert res.status_code == 200
    assert "fraud_probability" in res.json()
