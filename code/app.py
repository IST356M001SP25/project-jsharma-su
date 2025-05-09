import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Jets Players Stats",
    layout="centered"
)
st.title("Jets Players Stats")

data_dir = os.path.join(os.path.dirname(__file__), "../data")
passing = pd.read_json(os.path.join(data_dir, "passing.json"))
rushing = pd.read_json(os.path.join(data_dir, "rushing.json"))
receiving = pd.read_json(os.path.join(data_dir, "receiving.json"))

passing["Name"] = passing["Age"]

for df in [passing, rushing, receiving]:
    df["Yds"] = pd.to_numeric(df["Yds"], errors="coerce")
    df.dropna(subset=["Yds"], inplace=True)

st.sidebar.title("Filters")

category = st.sidebar.radio("Select Stat Category:", ("Passing", "Rushing", "Receiving"))

if category == "Passing":
    df = passing.copy()
elif category == "Rushing":
    df = rushing.copy()
else:
    df = receiving.copy()

if "Year" in df.columns:
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df["Year"].fillna(2023, inplace=True)
else:
    df["Year"] = 2023

df["Year"] = df["Year"].astype(int)

available_years = sorted(df["Year"].unique(), reverse=True)
selected_year = st.sidebar.selectbox("Year", available_years)
df = df[df["Year"] == selected_year]

if "Pos" in df.columns:
    positions = sorted(df["Pos"].dropna().unique())
    selected_pos = st.sidebar.selectbox("Position", ["All"] + positions)
    if selected_pos != "All":
        df = df[df["Pos"] == selected_pos]
else:
    selected_pos = "All"

player_list = df["Name"].dropna().unique()
selected_player = st.sidebar.selectbox("Player (optional)", ["All"] + sorted(player_list))
if selected_player != "All":
    df = df[df["Name"] == selected_player]

top_df = df.sort_values(by="Yds", ascending=False).head(5)

def plot_top_players(df, title):
    plt.figure(figsize=(8, 5))
    plt.bar(df["Name"], df["Yds"], color="seagreen")
    plt.title(title)
    plt.xlabel("Player")
    plt.ylabel("Yards")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(plt)

if df.empty:
    st.warning("No data available with the selected filters.")
else:
    subtitle = f"Top 5 {category} Leaders - {selected_year}"
    if selected_pos != "All":
        subtitle += f" ({selected_pos})"
    plot_top_players(top_df, subtitle)