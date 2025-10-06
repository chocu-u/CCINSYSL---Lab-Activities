import pandas as pd

def main():
    # Load the cleaned data
    df = pd.read_csv("cleaned_evidence.csv")

    # Ensure timestamp column exists
    if "timestamp" not in df.columns:
        raise ValueError("The file does not contain a 'timestamp' column.")

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Feature engineering
    df["hour_of_day"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.day_name()
    df["is_weekend"] = df["day_of_week"].isin(["Saturday", "Sunday"])

    # Save enhanced data
    df.to_csv("feature_engineered_evidence.csv", index=False)
    print("Feature engineering complete. File saved as feature_engineered_evidence.csv")

if __name__ == "__main__":
    main()
