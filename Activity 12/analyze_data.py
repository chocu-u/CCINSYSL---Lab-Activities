"""
analyze_data.py

Activity 12: Final Project Analysis
Applies Isolation Forest anomaly detection to the cleaned rental data and creates visualization.
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np

INPUT_FILE = "../Activity 11/final_project_cleaned_data.csv"
OUTPUT_ANOMALIES = "final_project_anomalies.csv"
OUTPUT_CHART = "final_project_chart.png"

def main():
    print("Loading cleaned data...")
    df = pd.read_csv(INPUT_FILE)
    
    print(f"Loaded {len(df)} records from {INPUT_FILE}")
    print(f"Columns: {list(df.columns)}")
    
    features = ['Duration_Difference', 'hour_of_day']
    
    df_valid = df[df[features].notna().all(axis=1)].copy()
    print(f"\nUsing {len(df_valid)} records with complete data for anomaly detection")
    
    X = df_valid[features].values
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    print("\nApplying Isolation Forest anomaly detection...")
    iso_forest = IsolationForest(
        contamination=0.1,
        random_state=42,
        n_estimators=100
    )
    
    predictions = iso_forest.fit_predict(X_scaled)
    anomaly_scores = iso_forest.score_samples(X_scaled)
    
    df_valid['anomaly_prediction'] = predictions
    df_valid['anomaly_score_ml'] = anomaly_scores
    df_valid['is_anomaly'] = df_valid['anomaly_prediction'] == -1
    
    num_anomalies = df_valid['is_anomaly'].sum()
    pct_anomalies = (num_anomalies / len(df_valid)) * 100
    print(f"Detected {num_anomalies} anomalies ({pct_anomalies:.1f}% of data)")
    
    anomalies_df = df_valid[df_valid['is_anomaly']].copy()
    anomalies_df = anomalies_df.sort_values('Duration_Difference', ascending=False)
    anomalies_df.to_csv(OUTPUT_ANOMALIES, index=False)
    print(f"\nSaved {len(anomalies_df)} anomalies to {OUTPUT_ANOMALIES}")
    
    print("\nTop 5 anomalies by Duration_Difference:")
    print(anomalies_df[['rental_id', 'customer_name_clean', 'Duration_Difference', 
                        'hour_of_day', 'non_return']].head())
    
    print("\nCreating visualization...")
    plt.figure(figsize=(12, 7))
    
    normal_data = df_valid[~df_valid['is_anomaly']]
    plt.scatter(normal_data['hour_of_day'], normal_data['Duration_Difference'], 
                c='lightblue', alpha=0.5, s=30, label='Normal Rentals', edgecolors='none')
    
    anomaly_data = df_valid[df_valid['is_anomaly']]
    plt.scatter(anomaly_data['hour_of_day'], anomaly_data['Duration_Difference'], 
                c='red', alpha=0.7, s=60, label='Anomalous Rentals', 
                edgecolors='darkred', linewidths=1)
    
    plt.xlabel('Hour of Day (Rental Start Time)', fontsize=12, fontweight='bold')
    plt.ylabel('Duration Difference (Actual - Expected Hours)', fontsize=12, fontweight='bold')
    plt.title('Anomalous Rental Duration vs. Time of Day\nCar Rental Fraud Detection Analysis', 
              fontsize=14, fontweight='bold', pad=20)
    plt.legend(loc='upper right', fontsize=10)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.xticks(range(0, 25, 2))
    
    plt.axhline(y=0, color='gray', linestyle='-', linewidth=0.8, alpha=0.5)
    
    stats_text = f"Total Records: {len(df_valid)}\n"
    stats_text += f"Anomalies Detected: {num_anomalies} ({pct_anomalies:.1f}%)\n"
    stats_text += f"Max Duration Difference: {df_valid['Duration_Difference'].max():.1f}h"
    
    plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes,
             fontsize=9, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig(OUTPUT_CHART, dpi=300, bbox_inches='tight')
    print(f"Saved visualization to {OUTPUT_CHART}")
    
    print("\n" + "="*60)
    print("ANALYSIS SUMMARY")
    print("="*60)
    print(f"Dataset: {INPUT_FILE}")
    print(f"Total records analyzed: {len(df_valid)}")
    print(f"Anomalies detected: {num_anomalies} ({pct_anomalies:.1f}%)")
    print(f"\nDuration Difference Statistics (Anomalies):")
    print(f"  Mean: {anomaly_data['Duration_Difference'].mean():.2f} hours")
    print(f"  Median: {anomaly_data['Duration_Difference'].median():.2f} hours")
    print(f"  Max: {anomaly_data['Duration_Difference'].max():.2f} hours")
    print(f"\nMost common rental hours for anomalies:")
    print(anomaly_data['hour_of_day'].value_counts().head())
    print(f"\nTop customers with anomalous rentals:")
    print(anomaly_data['customer_name_clean'].value_counts().head())
    print("\n" + "="*60)
    print("Analysis complete!")

if __name__ == '__main__':
    main()
