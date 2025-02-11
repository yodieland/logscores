import streamlit as st
import pandas as pd

# 📌 Path to your Excel file (hosted online or in repo)
FILE_URL = "https://raw.githubusercontent.com/yodieland/your-repo/main/scaled_metrics_with_scores.xlsx"

# 📌 Load all sheets into a dictionary
@st.cache_data
def load_data():
    xls = pd.ExcelFile(FILE_URL)
    dfs = {sheet: pd.read_excel(xls, sheet) for sheet in xls.sheet_names}
    return dfs

# Load data
dfs = load_data()

# Streamlit UI
st.set_page_config(page_title="City Scores Dashboard", layout="centered")
st.title("📊 City Metrics Score Dashboard")

# Dropdown for year selection
year = st.selectbox("Select Year", options=list(dfs.keys()))

# Get DataFrame for selected year
df = dfs[year]

# Ensure the correct columns exist
score_columns = ["NAME_CITY", "Social_Score", "Political_Score", "Economic_Score", "Environmental_Score", "Total_Score"]
df = df[score_columns] if set(score_columns).issubset(df.columns) else df

# Dropdown for city selection
selected_city = st.selectbox("Select City", df["NAME_CITY"].unique())

# Display selected city's scores
city_data = df[df["NAME_CITY"] == selected_city].iloc[0]

st.header(f"🏙️ {selected_city}")
st.subheader(f"Total Score: **{city_data['Total_Score']}**")
st.metric("🌍 Social Score", city_data["Social_Score"])
st.metric("🏛️ Political Score", city_data["Political_Score"])
st.metric("💰 Economic Score", city_data["Economic_Score"])
st.metric("🌱 Environmental Score", city_data["Environmental_Score"])

