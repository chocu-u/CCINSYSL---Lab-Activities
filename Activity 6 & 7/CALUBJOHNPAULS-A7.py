import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
 
anomalies_df = pd.read_csv('anomalies_detected_evidence.csv')
entities_df = pd.read_csv('extracted_entities.csv')
 
event_counts = anomalies_df['event_type'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(event_counts.index, event_counts.values, color='steelblue')
plt.title('Distribution of Event Types in Anomalous Data')
plt.xlabel('Event Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('event_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
 
report = f"""# Forensic Investigation Report
 
## Executive Summary
This report presents the findings of a comprehensive forensic analysis conducted on system logs. Through automated anomaly detection and entity extraction, we identified {len(anomalies_df)} anomalous events and extracted {len(entities_df)} key entities for further investigation.
 
## Methodology
The investigation followed a systematic approach:
1. **Data Preprocessing**: Raw log data was cleaned and standardized
2. **Feature Engineering**: Additional analytical features were created
3. **Anomaly Detection**: Statistical methods identified unusual patterns
4. **Entity Extraction**: Natural Language Processing (NLP) using SpaCy extracted key entities
 
## Key Findings
 
### Anomaly Analysis
- Total anomalous events detected: **{len(anomalies_df)}**
- Most common anomalous event type: **{event_counts.index[0]}** ({event_counts.values[0]} occurrences)
- Investigation period: {len(anomalies_df)} suspicious activities flagged
 
### Entity Extraction Results
- Total entities extracted: **{len(entities_df)}**
- Entity types found: {', '.join(entities_df['entity_label'].unique())}
- Key persons of interest: {len(entities_df[entities_df['entity_label'] == 'PERSON'])} individuals identified
- Geographic locations: {len(entities_df[entities_df['entity_label'] == 'GPE'])} locations flagged
 
## Data Visualization
![Event Distribution](event_distribution.png)
 
## Conclusion
The automated analysis has successfully identified patterns and entities requiring further investigation. The anomaly detection system flagged {len(anomalies_df)} events for manual review, while entity extraction provided {len(entities_df)} potential leads.
 
## Recommendations
1. Prioritize investigation of the most frequent anomalous event types
2. Cross-reference extracted entities with known databases
3. Conduct deeper analysis on flagged time periods
4. Implement continuous monitoring based on identified patterns
 
*Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
with open('forensic_report.md', 'w') as f:
    f.write(report)
 
print("Final report generated successfully!")
print("Files created:")
print("- event_distribution.png")
print("- forensic_report.md")