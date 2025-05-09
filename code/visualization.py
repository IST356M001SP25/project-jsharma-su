import pandas as pd
import matplotlib.pyplot as plt
import os
import json

data_dir = os.path.join(os.path.dirname(__file__), "../data")

passing = pd.read_json(os.path.join(data_dir, "passing.json"))
rushing = pd.read_json(os.path.join(data_dir, "rushing.json"))
receiving = pd.read_json(os.path.join(data_dir, "receiving.json"))

passing['Yds'] = pd.to_numeric(passing['Yds'], errors='coerce')
rushing['Yds'] = pd.to_numeric(rushing['Yds'], errors='coerce')
receiving['Yds'] = pd.to_numeric(receiving['Yds'], errors='coerce')

passing = passing.dropna(subset=['Yds'])
rushing = rushing.dropna(subset=['Yds'])
receiving = receiving.dropna(subset=['Yds'])

top_passers = passing.sort_values(by='Yds', ascending=False).head(5)
top_rushers = rushing.sort_values(by='Yds', ascending=False).head(5)
top_receivers = receiving.sort_values(by='Yds', ascending=False).head(5)

def plot_top_players(df, title, stat_col='Yds'):
    plt.figure(figsize=(8, 5))
    plt.bar(df['Player'], df[stat_col], color='steelblue')
    plt.title(title)
    plt.xlabel("Player")
    plt.ylabel("Yards")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_top_players(top_passers, "Top 5 Passers (by Yards)")
plot_top_players(top_rushers, "Top 5 Rushers (by Yards)")
plot_top_players(top_receivers, "Top 5 Receivers (by Yards)")
