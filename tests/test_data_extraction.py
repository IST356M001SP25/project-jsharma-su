import json
import os

def test_data_extraction():
    cache_dir = os.path.join(os.path.dirname(__file__), "../cache")
    output_path = os.path.join(cache_dir, "jets_stats.json")

    assert os.path.exists(output_path), "Data extraction failed, file not found!"

    with open(output_path, 'r') as f:
        extracted_data = json.load(f)

    assert 'team_stats' in extracted_data, "Missing 'team_stats' table!"
    assert 'passing' in extracted_data, "Missing 'passing' table!"
    assert len(extracted_data['team_stats']) > 0, "No data in 'team_stats' table!"
    assert len(extracted_data['passing']) > 0, "No data in 'passing' table!"
