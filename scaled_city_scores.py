import streamlit as st
import pandas as pd
st.set_page_config(page_title="City Metrics Dashboard", layout="centered")
# Load the data
FILE_PATH = r"C:scaled_metrics_with_scores.xlsx"


@st.cache_data
def load_data():
    return pd.read_excel(FILE_PATH)

df = load_data()

# Streamlit UI - Credit Score Style


# App Title
st.markdown(
    "<h1 style='text-align: center; font-size: 40px; color: #1f77b4;'>City Metrics Dashboard</h1>",
    unsafe_allow_html=True,
)

# Dropdown for city selection
city_name = st.selectbox(
    "Select a City", df["NAME_CITY"].unique(), index=0, help="Choose a city to view its metrics."
)

# Filter data for the selected city
city_data = df[df["NAME_CITY"] == city_name]

if not city_data.empty:
    total_score = city_data["Total_Score"].values[0]

    # **Main Credit Score Display**
    st.markdown(
        f"""
        <div style="text-align: center;">
            <div style="font-size: 50px; font-weight: bold; color: #ff5733;">{total_score:.2f}</div>
            <div style="font-size: 20px; color: #555;">Total Score</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # **Four Subscores (Displayed Like a Credit Score Breakdown)**
    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(label="📊 Social Score", value=f"{city_data['Social_Score'].values[0]:.2f}")
    col2.metric(label="🏛️ Political Score", value=f"{city_data['Political_Score'].values[0]:.2f}")
    col3.metric(label="💰 Economic Score", value=f"{city_data['Economic_Score'].values[0]:.2f}")
    col4.metric(label="🌿 Environmental Score", value=f"{city_data['Environmental_Score'].values[0]:.2f}")

    st.markdown("<hr>", unsafe_allow_html=True)

else:
    st.error("City not found!")

# Footer
st.markdown(
    "<p style='text-align: center; font-size: 14px; color: gray;'>Developed with ❤️ using Streamlit</p>",
    unsafe_allow_html=True,
)
