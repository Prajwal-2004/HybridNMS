# train_model.py
import pandas as pd
import lightgbm as lgb
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load data
df = pd.read_csv('../data/telemetry.csv')

# Feature engineering
X = df[['latency_ms', 'throughput_mbps', 'packet_loss_percent']]
y = df['latency_ms']  # Example target: predicting latency (can adapt to action selection)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = lgb.LGBMRegressor()
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)
print(f"Test MSE: {mse}")

# Save model
joblib.dump(model, '../ml/latency_model.pkl')
print("Model saved as latency_model.pkl")
