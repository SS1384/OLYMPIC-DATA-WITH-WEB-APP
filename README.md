# 🏅 Olympics EDA Dashboard

An interactive Exploratory Data Analysis (EDA) dashboard built with Python and Streamlit to visualize over a century of historical Olympic Games data. 

## 📝 Overview
This project transforms raw historical Olympic data (`athlete_events.csv`) into an interactive web application. Users can filter data by specific years and countries (NOC) to instantly view historical medal tallies and visual breakdowns of Gold, Silver, and Bronze achievements.

## ✨ Features
* **Interactive Filtering:** Select any participating country and Olympic year via dropdown menus.
* **Dynamic Data Aggregation:** Real-time calculation of Gold, Silver, Bronze, and Total medals using Pandas.
* **Data Visualization:** Clean, dynamically generated bar charts built with Matplotlib.
* **Error Handling:** Built-in safeguards to gracefully handle missing data for years without Olympic events.

## 🛠️ Tech Stack
* **Language:** Python
* **Web Framework:** Streamlit
* **Data Manipulation:** Pandas
* **Data Visualization:** Matplotlib

## 📂 Project Structure
```text
📦 EDAMAJORPROJECT
 ┣ 📂 App
 ┃ ┣ 📂 data
 ┃ ┃ ┣ 📜 app.py               # Main Streamlit frontend script
 ┃ ┃ ┣ 📜 helper.py            # Backend logic, data filtering, and plotting functions
 ┃ ┃ ┗ 📜 athlete_events.csv   # Project dependencies
 ┃ ┗ 📜 requirements.txt      
 ┗ 📜 README.md
