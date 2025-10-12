from datetime import datetime, timedelta
import csv
import random

OUT = "final_project_raw_data.csv"
NUM_RECORDS = 150

vehicle_models = [
    "Toyota Corolla", "Honda Civic", "Mitsubishi Lancer", "Toyota Fortuner",
    "BYD Seal", "Nissan Altima", "BMW M3", "Audi A4"
]
first_names = ["John", "Jane", "Alex", "Chris", "Pat", "Taylor", "Sam", "Jordan"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis"]

def random_name():
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    if random.random() < 0.2:
        return name.upper()
    if random.random() < 0.2:
        return name.lower()
    return name.title()

def main():
    start_date = datetime(2025, 1, 1)
    rows = []
    for i in range(1, NUM_RECORDS + 1):
        rental_id = f"R{i:05d}"
        customer_name = random_name()
        rent_out = start_date + timedelta(hours=random.randint(0, 24*180), minutes=random.randint(0,59))
        expected = round(random.uniform(1, 72), 1)

        r = random.random()
        if r < 0.03:
            return_ts = ""
            actual = ""
        else:
            if r < 0.85:
                actual_hours = expected * random.uniform(0.5, 1.5)
            elif r < 0.98:
                actual_hours = expected * random.uniform(1.5, 6)
            else:
                actual_hours = expected * random.uniform(6, 40)
            return_ts = (rent_out + timedelta(hours=actual_hours, minutes=random.randint(0,59))).isoformat()
            actual = round(actual_hours, 1)

        vehicle = random.choice(vehicle_models)

        rows.append({
            "rental_id": rental_id,
            "customer_name": customer_name,
            "rent_out_timestamp": rent_out.isoformat(),
            "return_timestamp": return_ts,
            "rental_duration_hours": expected,
            "actual_duration_hours": actual,
            "vehicle_make_model": vehicle,
        })

    fieldnames = [
        "rental_id", "customer_name", "rent_out_timestamp", "return_timestamp",
        "rental_duration_hours", "actual_duration_hours", "vehicle_make_model"
    ]
    with open(OUT, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    print(f"Wrote {len(rows)} records to {OUT}")

if __name__ == '__main__':
    main()
