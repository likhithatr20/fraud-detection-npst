import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/transactions.csv")

FEATURES = [
    "amount",
    "hour",
    "day_of_week",
    "distance_from_home"
]

X = df[FEATURES]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = IsolationForest(
    n_estimators=100,
    contamination=0.02,
    random_state=42
)

model.fit(X_scaled)

joblib.dump((model, scaler), "models/isolation_forest.pkl")

print("Model trained and saved")
