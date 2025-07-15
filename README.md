# 🌾 Global Agricultural Sustainability Dashboard

This project is an interactive dashboard built with **Streamlit** to visualize key indicators of agricultural sustainability across selected countries. It allows users to upload their datasets and explore various agricultural metrics such as GHG emissions, fertilizer use, crop production, and food supply trends.

---

## 🚀 Features

- 📊 Visualize greenhouse gas (GHG) emissions from agriculture by country and over time
- 🌱 Analyze fertilizer usage trends by nutrient and country
- 🌾 Explore crop production data and its correlation with fertilizer use
- 🍽️ Examine food supply metrics
- 🗂️ Interactive interface with tab-based navigation

---

## 📁 Required Input Files

The app expects the following CSV files (upload via sidebar):

- `Emission final.csv`
- `Fertilizers by Nutrient final.csv`
- `Crops and Livestock products final.csv`
- `Food Supply final.csv`

Make sure each file includes:
- A `Year` column (2010–2022)
- An `Area` column with country names
- Relevant columns depending on the metric (e.g., `Value`, `Item`, `Element`)

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)

---

## ▶️ Running the App

To run the dashboard locally:

```bash
pip install streamlit pandas matplotlib seaborn
streamlit run app.py
```

---

## 📌 Note

Please upload **all four datasets** to start using the dashboard. If any file is missing, the app will display a warning.


