# Streamlit version of your agricultural sustainability dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Setup ---
st.set_page_config(page_title="🌾 Global Agriculture Dashboard", layout="wide")
st.title("🌍 Global Agricultural Sustainability Dashboard")

# --- Load Data ---
st.sidebar.header("Upload CSV Files")
emissions_file = st.sidebar.file_uploader("Emission final", type="csv")
fertilizers_file = st.sidebar.file_uploader(
    "Fertilizers by Nutrient final", type="csv")
crops_file = st.sidebar.file_uploader(
    "Crops and Livestock products final", type="csv")
food_supply_file = st.sidebar.file_uploader("Food Supply final", type="csv")

if all([emissions_file, fertilizers_file, crops_file, food_supply_file]):
    emissions = pd.read_csv(emissions_file)
    fertilizers = pd.read_csv(fertilizers_file)
    crops = pd.read_csv(crops_file)
    food_supply = pd.read_csv(food_supply_file)

    target_countries = [
        'Brazil', 'China', 'Ethiopia', 'India', 'Israel',
        'Netherlands (Kingdom of the)', 'Rwanda',
        'United Arab Emirates', 'United States of America', 'Viet Nam'
    ]

    for df in [emissions, fertilizers, crops, food_supply]:
        df.query("2010 <= Year <= 2022", inplace=True)
        df.query("Area in @target_countries", inplace=True)

    tabs = st.tabs([f"Q{i+1}" for i in range(8)])

    with tabs[0]:
        st.subheader(
            "Q1: Which countries emit the most GHGs from agriculture?")
        df = emissions[emissions["Element"] == "Emissions (CO2eq) (AR5)"]
        chart = df.groupby("Area")["Value"].sum(
        ).reset_index().sort_values("Value", ascending=False)
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=chart, x="Value", y="Area", palette="Reds", ax=ax)
        ax.set_title("Total Agricultural GHG Emissions by Country")
        st.pyplot(fig)

    with tabs[1]:
        st.subheader("Q2: Emission trends over time")
        df = emissions[emissions["Element"] == "Emissions (CO2eq) (AR5)"]
        chart = df.groupby(["Area", "Year"])["Value"].sum().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=chart, x="Year", y="Value",
                     hue="Area", marker="o", ax=ax)
        ax.set_title("Agricultural GHG Emissions Over Time")
        st.pyplot(fig)

    with tabs[2]:
        st.subheader("Q3: Emission sources")
        df = emissions[emissions["Element"] == "Emissions (CO2eq) (AR5)"]
        chart = df.groupby("Item")["Value"].sum(
        ).reset_index().sort_values("Value", ascending=False)
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(chart["Value"], labels=chart["Item"],
               autopct="%1.1f%%", startangle=140)
        ax.set_title("Emission Sources Share")
        st.pyplot(fig)

    with tabs[3]:
        st.subheader("Q4: Fertilizer use by nutrient")
        df = fertilizers[(fertilizers["Element"] == "Agricultural Use") & (
            fertilizers["Item"].str.contains("Nutrient"))]
        chart = df.groupby(["Year", "Item"])["Value"].sum().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=chart, x="Year", y="Value",
                     hue="Item", marker="o", ax=ax)
        ax.set_title("Global Fertilizer Use by Nutrient")
        st.pyplot(fig)

    with tabs[4]:
        st.subheader("Q5: Fertilizer use trends by country")
        df = fertilizers[fertilizers["Element"] == "Agricultural Use"]
        chart = df.groupby(["Area", "Year"])["Value"].sum().reset_index()
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=chart, x="Year", y="Value",
                     hue="Area", marker="o", ax=ax)
        ax.set_title("Fertilizer Use by Country Over Time")
        st.pyplot(fig)

    with tabs[5]:
        st.subheader("Q6A: Nitrogen use per hectare")
        df = fertilizers[(fertilizers["Element"] == "Use per area of cropland") & (
            fertilizers["Item"] == "Nutrient nitrogen N (total)")]
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=df, x="Year", y="Value",
                     hue="Area", marker="o", ax=ax)
        ax.set_title("Nitrogen Fertilizer Use per Hectare")
        st.pyplot(fig)

    with tabs[6]:
        st.subheader("Q6B: Nitrogen use per capita")
        df = fertilizers[(fertilizers["Element"] == "Use per capita") & (
            fertilizers["Item"] == "Nutrient nitrogen N (total)")]
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.lineplot(data=df, x="Year", y="Value",
                     hue="Area", marker="o", ax=ax)
        ax.set_title("Nitrogen Fertilizer Use per Capita")
        st.pyplot(fig)

    with tabs[7]:
        st.subheader("Q7: Fertilizer vs Crop Production")
        fert = fertilizers[(fertilizers["Element"] == "Agricultural Use") & (
            fertilizers["Item"] == "Nutrient nitrogen N (total)") & (fertilizers["Year"] == 2022)]
        crop = crops[(crops["Element"] == "Production")
                     & (crops["Year"] == 2022)]
        crop_sum = crop.groupby("Area")["Value"].sum().reset_index()
        fert_crop = pd.merge(
            fert[["Area", "Value"]], crop_sum, on="Area", suffixes=("_fert", "_crop"))
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=fert_crop, x="Value_fert",
                        y="Value_crop", hue="Area", s=100, ax=ax)
        ax.set_xlabel("Nitrogen Fertilizer Use (Tonnes)")
        ax.set_ylabel("Crop Production (Tonnes)")
        ax.set_title("Fertilizer Use vs. Crop Production")
        st.pyplot(fig)

else:
    st.warning("Please upload all required datasets to begin.")
