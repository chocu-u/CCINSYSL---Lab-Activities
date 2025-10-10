# Activity 10: Final Project Data Prep

This folder contains two scripts to create and preprocess the simulated rental fraud dataset for the final project.

Files:
- `generate_data.py`: generates `rental_fraud_log.csv` (500 records by default).
- `preprocess_data.py`: reads `rental_fraud_log.csv`, performs cleaning and feature engineering, and writes `final_project_cleaned_data.csv` and `final_project_anomalies.csv`.
- `requirements.txt`: dependencies.

Usage (Windows PowerShell):

```powershell
python -m pip install -r requirements.txt
python generate_data.py
python preprocess_data.py
```

Outputs:
- `rental_fraud_log.csv` (raw simulated logs)
- `final_project_cleaned_data.csv` (cleaned, feature-engineered)
- `final_project_anomalies.csv` (rows flagged as anomalous)
