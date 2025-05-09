import pandas as pd
import os

def test_visualization_data_loading():
    data_dir = os.path.join(os.path.dirname(__file__), "../data")

    passing = pd.read_json(os.path.join(data_dir, "passing.json"))
    rushing = pd.read_json(os.path.join(data_dir, "rushing.json"))
    receiving = pd.read_json(os.path.join(data_dir, "receiving.json"))

    passing['Yds'] = pd.to_numeric(passing['Yds'], errors='coerce')
    rushing['Yds'] = pd.to_numeric(rushing['Yds'], errors='coerce')
    receiving['Yds'] = pd.to_numeric(receiving['Yds'], errors='coerce')

    top_passers = passing.dropna(subset=['Yds']).sort_values(by='Yds', ascending=False).head(5)
    top_rushers = rushing.dropna(subset=['Yds']).sort_values(by='Yds', ascending=False).head(5)
    top_receivers = receiving.dropna(subset=['Yds']).sort_values(by='Yds', ascending=False).head(5)

    assert not top_passers.empty, "Top passers list is empty!"
    assert not top_rushers.empty, "Top rushers list is empty!"
    assert not top_receivers.empty, "Top receivers list is empty!"