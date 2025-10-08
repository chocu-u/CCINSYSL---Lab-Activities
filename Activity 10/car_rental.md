# Final Project Plan: Car Rental Logger System Forensics

## 1. Summary of Course Project (Weeks 1-6)

The progressive project established a complete forensic workflow: **data generation and preprocessing** (Weeks 1-3) to create a clean, feature-enriched dataset. The analysis phase (Weeks 4-5) involved applying **Anomaly Detection (Isolation Forest)** to find suspicious events and **Named Entity Recognition (NER)** to structure textual clues. The project concluded with professional **reporting and visualization** (Week 6), successfully translating technical data into actionable forensic intelligence.

---

## 2. Final Project Plan

### A. Data Description: Raw Evidence Simulation

* **File Name:** `rental_fraud_log.csv`
* **Contents:** Transaction logs tracking rentals, returns, and customer data, focused on **identifying fraud** (e.g., unauthorized or excessive late use).
* **Key Columns:** `rental_id`, `customer_name`, `rent_out_timestamp`, `return_timestamp`, `rental_duration_hours` (expected), and `vehicle_make_model`.
* **Simulated Issues:** Missing `return_timestamp` for fraudulent non-returns, and inconsistent text casing in `customer_name`.

### B. Step-by-Step Preprocessing Strategy

The goal is to produce **`final_project_cleaned_data.csv`**.

1.  **Type Conversion:** Convert all timestamp columns to `datetime` objects and `rental_duration_hours` to a numerical (float) type.
2.  **Missing Data Handling:** For missing `return_timestamp`, calculate a large default `Actual Duration` (e.g., 999 hours) and flag it as a potential **"Non-Return"**.
3.  **Feature Engineering:**
    * Calculate the core feature: **`Duration_Difference`** (Actual Duration - Expected Duration).
    * Extract `hour_of_day` and `is_weekend` from the rent-out timestamp.
4.  **Standardization:** Standardize the text in the `customer_name` column (e.g., convert to Title Case).

### C. Intelligent Analysis Plan

The objective is to identify suspicious rentals indicative of fraud or abuse.

| Analysis Technique | Purpose/Question | Features Used | Output Artifact |
| :--- | :--- | :--- | :--- |
| **Anomaly Detection** (Isolation Forest) | **Detect rentals with extreme Duration Differences (excessive lateness) or highly unusual rental times.** | Normalized `Duration_Difference`, `hour_of_day`. | `final_project_anomalies.csv` |
| **Named Entity Recognition (NER)** (SpaCy) | **Extract full names from `customer_name` to identify and link repeat offenders.** | `customer_name` (text column) | Structured list of extracted customer entities. |

### D. Visualization Strategy

The visualization will clearly show the relationship between the time of rental and the severity of the anomaly.

1.  **Visualization:** **Duration Scatter Plot** plotting the calculated **`Duration_Difference`** (y-axis) against the `hour_of_day` (x-axis).
2.  **Highlight:** **Anomalous points** (flagged rentals) will be plotted in a distinct color to visually demonstrate that highly unusual rentals often began during late or off-peak hours.
3.  **Output:** **`final_project_chart.png`** (Anomalous Rental Duration vs. Time of Day).

### E. Key Conclusions for Final Report

The final report will detail the findings and offer recommendations.

1.  **Fraud Pattern:** Establish that a pattern of **excessively late and non-returned vehicles** exists, often initiated outside of normal business hours.
2.  **Anomalous Events:** Quantify the percentage of rentals flagged as anomalous and identify the specific **`rental_id`s** and **`customer_name`s** associated with the highest `Duration_Difference` values.
3.  **Remediation:** Recommend immediate automated flagging for rentals exceeding a set duration threshold and a manual review of all customer accounts identified as anomalous by the model.
