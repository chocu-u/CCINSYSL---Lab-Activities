import pandas as pd
from datetime import datetime

IN = "final_project_raw_data.csv"
OUT = "final_project_cleaned_data.csv"
ANOM = "final_project_anomalies.csv"

def main():
    df = pd.read_csv(IN)

    df['rent_out_timestamp'] = pd.to_datetime(df['rent_out_timestamp'], errors='coerce')
    df['return_timestamp'] = pd.to_datetime(df['return_timestamp'], errors='coerce')

    df['non_return'] = df['return_timestamp'].isna()
    df.loc[df['non_return'], 'actual_duration_hours'] = 999.0

    df['rental_duration_hours'] = pd.to_numeric(df['rental_duration_hours'], errors='coerce')
    df['actual_duration_hours'] = pd.to_numeric(df['actual_duration_hours'], errors='coerce')

    df['Duration_Difference'] = df['actual_duration_hours'] - df['rental_duration_hours']
    df['hour_of_day'] = df['rent_out_timestamp'].dt.hour.fillna(-1).astype(int)
    df['is_weekend'] = df['rent_out_timestamp'].dt.dayofweek.isin([5,6])

    df['customer_name_clean'] = df['customer_name'].fillna('').str.strip().str.title()

    df['anomaly_score'] = 0.0
    df.loc[df['Duration_Difference'].notna(), 'anomaly_score'] = df.loc[df['Duration_Difference'].notna(), 'Duration_Difference'] / (df['rental_duration_hours'].replace(0,1))
    df.loc[df['non_return'], 'anomaly_score'] += 10

    df['anomaly'] = df['anomaly_score'] > 3.0

    cols_out = [
        'rental_id', 'customer_name', 'customer_name_clean', 'rent_out_timestamp', 'return_timestamp',
        'rental_duration_hours', 'actual_duration_hours', 'Duration_Difference', 'hour_of_day', 'is_weekend', 'non_return', 'anomaly_score', 'anomaly', 'vehicle_make_model'
    ]
    df.to_csv(OUT, index=False, columns=cols_out)

    df[df['anomaly']].to_csv(ANOM, index=False)

    print(f"Wrote cleaned data to {OUT} ({len(df)} rows)")
    print(f"Wrote anomalies to {ANOM} ({df['anomaly'].sum()} rows)")

if __name__ == '__main__':
    main()
