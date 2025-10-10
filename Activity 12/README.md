# Activity 12: Final Project Analysis

This folder contains the intelligent analysis script for the final project.

## Files
- `analyze_data.py`: Applies Isolation Forest anomaly detection to cleaned rental data and creates visualization
- `requirements.txt`: Python dependencies

## Prerequisites
Ensure you have the cleaned data file from Activity 11:
- `../Activity 11/final_project_cleaned_data.csv`

## Usage (Windows PowerShell)

```powershell
cd 'c:\Users\choco\Documents\GitHub\CCINSYSL-Lab-Activities\Activity 12'
python -m pip install -r requirements.txt
python analyze_data.py
```

## Outputs
- `final_project_anomalies.csv`: Records flagged as anomalous by Isolation Forest
- `final_project_chart.png`: Visualization showing Duration Difference vs Hour of Day with anomalies highlighted in red

## Analysis Details
The script uses **Isolation Forest** algorithm to detect anomalies based on:
- Duration_Difference (Actual - Expected rental hours)
- hour_of_day (Time when rental started)

The visualization clearly shows which rentals are fraudulent/suspicious and identifies patterns in rental timing.
