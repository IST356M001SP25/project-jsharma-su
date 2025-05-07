import json
import os

def load_raw_stats(filename="cache/jets_stats.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def clean_stats(raw_stats):
    cleaned = {}

    for key, value in raw_stats.items():
        clean_key = key.strip().lower().replace(" ", "_").replace("%", "percent")

        value = value.replace(",", "")
        try:
            if "." in value:
                clean_value = float(value)
            else:
                clean_value = int(value)
        except ValueError:
            clean_value = value

        cleaned[clean_key] = clean_value
    return cleaned

def save_cleaned_stats(stats, filename="cache/jets_cleaned_stats.json"):
    with open(filename, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Saved cleaned stats to {filename}")

if __name__ == "__main__":
    raw_stats = load_raw_stats()
    cleaned_stats = clean_stats(raw_stats)
    save_cleaned_stats(cleaned_stats)