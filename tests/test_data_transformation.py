import os
import json

def test_data_transformation():
    data_dir = os.path.join(os.path.dirname(__file__), "../data")
    expected_files = ["team_stats.json", "passing.json"]

    for filename in expected_files:
        file_path = os.path.join(data_dir, filename)
        assert os.path.exists(file_path), f"{filename} not found in /data directory!"

        with open(file_path, 'r') as f:
            data = json.load(f)
            assert isinstance(data, list), f"{filename} content is not a list!"
            assert len(data) > 0, f"{filename} is empty!"