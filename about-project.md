# About My Project

Student Name:  Jiya Sharma
Student Email:  jsharma@syr.edu

### What it does
This project is a Streamlit-based web dashboard that displays player statistics for the New York Jets in the year 2023. It provides visualizations as in the bar graph and interactive elements like choosing to analyze the passing yards, receiving yards, and the rushing yards, which help to explore data for the categories for the 2023 season.

The code I wrote extracts data. It uses web scraping with Playwright to pull New York Jets player stats from a website for pro football reference website with data from their 2023 season. The extracted data is saved in the 'cache' folder. The next thing the code does it transforms the data. The transformation page parses and organzies the scraped data into structured JSON files stored in the 'data' folder. The next page was the visualization page where that code is used to load and structure the data using Pandas and presents it using Plotly Expresss in a Streamlit interface. Lastly the app page is where the Streamlit was created whcih displays bar charts for top passers, rushers, and receivers, allowing users to easily understand the team performance in that season. I used Python, Streamlit, Pandas, Plotly, and Playwright (for web scraping).

### How you run my project
First, the requirements need to be installed. In the terminal write 'pip install -r requirements.txt' and click enter. Then write 'playwright install' after and click enter again. To run the Streamlit app, in your terminal write 'streamlit run code/app.py and press enter. Next, run the tests by writing in the terminal 'pytest tests/' Make sure each page of code, 'data_extraction.py', 'data_transformation.py', and 'visualizations.py' were run previous to running the Streamlit app.

### Other things you need to know
The folder structure is written as so. The code folder has all of the main Python scripts for extraction, transformation, and the streamlit app. The tests foler has all of the unit tests that are compatible with Pytest. the cache folder contains the raw scraped data. The data folder then contains all of the cleaned and transformed data that is used by the dashboard.