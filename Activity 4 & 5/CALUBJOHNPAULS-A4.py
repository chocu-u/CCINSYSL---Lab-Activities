import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the feature engineered evidence CSV file
input_file = 'feature_engineered_evidence.csv'
output_file = 'anomalies_detected_evidence.csv'

# Read the data
df = pd.read_csv(input_file)

# Initialize Isolation Forest
iso_forest = IsolationForest(random_state=42)

# Select only numeric columns for Isolation Forest
numeric_df = df.select_dtypes(include=['number'])

# Fit and predict anomalies (-1 for anomaly, 1 for normal)
df['is_anomaly'] = iso_forest.fit_predict(numeric_df)

# Save the results to a new CSV file
df.to_csv(output_file, index=False)

print(f"Anomaly detection complete. Results saved to {output_file}.")