import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

url = 'https://www.pro-football-reference.com/teams/nyj/2023.htm'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table_ids = ['team_stats', 'passing', 'rushing', 'receiving']
extracted_data = {}

for table_id in table_ids:
    table = soup.find('table', id=table_id)
    if not table:
        print(f"Table with ID '{table_id}' not found.")
        continue

    headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]
    headers = headers[1:]

    rows = []
    for row in table.find('tbody').find_all('tr'):
        if row.get('class') == ['thead']:
            continue
        cols = row.find_all(['td', 'th'])
        if not cols:
            continue
        row_data = [col.get_text(strip=True) for col in cols]
        rows.append(dict(zip(headers, row_data)))

    extracted_data[table_id] = rows

cache_dir = os.path.join(os.path.dirname(__file__), "../cache")
os.makedirs(cache_dir, exist_ok=True)

for table_id, data in extracted_data.items():
    output_path = os.path.join(cache_dir, f"{table_id}.json")
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {table_id} data to {output_path}")

print(f"Successfully saved extracted tables to {output_path}")