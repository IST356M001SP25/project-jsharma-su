# code/data_extraction.py

import requests
from bs4 import BeautifulSoup
import json
import os

def get_jets_stats():
    url = "https://www.pro-football-reference.com/teams/nyj/2023.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.114 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    with open("cache/raw.data.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())
        print("Saved raw HTML to cache/raw.data.html")

    return soup

def extract_stats(soup):
    stats = {}

    table = soup.find("table", id="team_stats")
    if table is None:
        print("Warning: Could not find table with id='team_stats'")
        return stats
    
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) == 2:
            stat_name = cells[0].text.strip()
            stat_value = cells[1].text.strip()
            stats[stat_name] = stat_value

    return stats

def save_stats_to_json(stats, filename="cache/jets_stats.json"):
    os.makedirs("cache", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Saved stats to {filename}")

if __name__ == "__main__":
    soup = get_jets_stats()
    stats = extract_stats(soup)
    save_stats_to_json(stats)
