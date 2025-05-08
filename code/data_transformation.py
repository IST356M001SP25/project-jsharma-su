import json
import os
import pandas as pd

CACHE_DIR = os.path.join(os.path.dirname(__file__), "../cache")
INPUT_FILE = os.path.join(CACHE_DIR, "jets_stats.json") 
OUTPUT_FILE = os.path.join(CACHE_DIR, "jets_cleaned_stats.json")  

def transform_data():
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    print(f"Data type: {type(data)}")  
    print(f"Keys in data: {data.keys()}")  

    all_data = []
    for key in data.keys():
        if isinstance(data[key], list):
            for entry in data[key]:
                if isinstance(entry, dict): 
                    all_data.append(entry)
                else:
                    print(f"Warning: Entry in {key} is not a dictionary: {entry}")
        else:
            print(f"Warning: Data under {key} is not a list.")

    expected_columns = ["Wins", "Losses", "Points For", "Points Against"]
    for entry in all_data:
        for column in expected_columns:
            if column not in entry:
                entry[column] = None 

    df = pd.DataFrame(all_data)

    df.fillna(0, inplace=True)

    df["Wins"] = df["Wins"].astype(int)
    df["Losses"] = df["Losses"].astype(int)
    df["Points For"] = df["Points For"].astype(int)
    df["Points Against"] = df["Points Against"].astype(int)

    df.to_json(OUTPUT_FILE, orient="records", indent=2)

    print(f" Transformed data written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    transform_data()