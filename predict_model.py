# predict_model.py
import pandas as pd
import joblib
import shap

# Load model
model = joblib.load('latency_model.pkl')

# Load new telemetry data
df_new = pd.read_csv('../data/telemetry.csv')
X_new = df_new[['latency_ms', 'throughput_mbps', 'packet_loss_percent']]

# Predict
preds = model.predict(X_new)
df_new['predicted_latency'] = preds

# Explainability with SHAP
explainer = shap.Explainer(model)
shap_values = explainer(X_new)

shap.summary_plot(shap_values, X_new)  # This opens a matplotlib summary

# Save predictions
df_new.to_csv('../logs/predictions.csv', index=False)
print("Predictions saved to logs/predictions.csv")
