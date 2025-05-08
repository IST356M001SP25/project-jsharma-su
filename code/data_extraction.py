import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = 'https://www.pro-football-reference.com/teams/nyj/2023.htm'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table')

all_tables_data = {}

for i, table in enumerate(tables):
    print(f"Processing Table {i}: {table.caption.string if table.caption else 'No caption'}")
    
    headers = [header.get_text(strip=True) for header in table.find_all('th')]
    print(f"Headers found: {headers}")

    rows = []

    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        
        if len(columns) == len(headers):
            rows.append([col.get_text(strip=True) for col in columns])
        else:
            print(f"Skipping row due to mismatched columns: {[col.get_text(strip=True) for col in columns]}")
            if len(columns) < len(headers):
                columns.extend([None] * (len(headers) - len(columns)))
            elif len(columns) > len(headers):
                columns = columns[:len(headers)]
            
            rows.append([col.get_text(strip=True) if col else None for col in columns])

    df = pd.DataFrame(rows, columns=headers)

    all_tables_data[f"table_{i}"] = df.to_dict(orient="records")

with open('jets_stats.json', 'w') as json_file:
    json.dump(all_tables_data, json_file, indent=4)

print("Tables have been successfully saved in jets_stats.json.")
