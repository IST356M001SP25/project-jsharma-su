import pandas as pd
import json
import os

cache_dir = os.path.join(os.path.dirname(__file__), "../cache")
input_path = os.path.join(cache_dir, "jets_stats.json")
with open(input_path, 'r') as f:
    raw_data = json.load(f)

cleaned_data = {}

def clean_dataframe(table_data):
    df = pd.DataFrame(table_data)
    df = df.dropna(how='all')
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')
    return df

for key, table in raw_data.items():
    cleaned_df = clean_dataframe(table)
    cleaned_data[key] = cleaned_df

output_dir = os.path.join(os.path.dirname(__file__), "../data")
os.makedirs(output_dir, exist_ok=True)

for key, df in cleaned_data.items():
    df.to_json(os.path.join(output_dir, f"{key}.json"), orient="records", indent=2)

all_data_path = os.path.join(output_dir, "jets_stats_cleaned.json")
with open(all_data_path, 'w') as f:
    json.dump({k: v.to_dict(orient="records") for k, v in cleaned_data.items()}, f, indent=2)

print("Cleaned data saved to /data directory.")