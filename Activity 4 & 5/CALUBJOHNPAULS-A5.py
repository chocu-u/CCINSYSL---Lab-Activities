import pandas as pd
import spacy

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Load the CSV file
input_file = "anomalies_detected_evidence.csv"
df = pd.read_csv(input_file)

# Prepare a list to store extracted entities
entities_list = []

# Process each message for entities
for idx, row in df.iterrows():
    message = str(row.get("message", ""))
    doc = nlp(message)
    for ent in doc.ents:
        entities_list.append({
            "message_id": idx,
            "message": message,
            "entity_text": ent.text,
            "entity_label": ent.label_
        })

# Save extracted entities to CSV
output_file = "extracted_entities.csv"
entities_df = pd.DataFrame(entities_list)
entities_df.to_csv(output_file, index=False)

print(f"Extracted entities saved to {output_file}")