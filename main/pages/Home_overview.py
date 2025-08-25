import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Railway Accident Analytics - Overview", layout="wide")

# --- Dataset Loading from GitHub ---

# Dictionary of datasets available in the GitHub repository
# I've updated the keys to match your new file names for clarity
DATASETS = {
    "Main Cleaned Data (1900-2024)": "https://raw.githubusercontent.com/yashhackz360/Railway_Accdeint_Analytics_A_data_driven_AI_Approach/main/Assests/train_Accident_1900_2024_cleaned.csv",
    "Analysis Dataset": "https://raw.githubusercontent.com/yashhackz360/Railway_Accdeint_Analytics_A_data_driven_AI_Approach/main/Assests/train_accident_analysis%20dataset.csv", # Note: I'm assuming this is a CSV. Update if it's another format.
    "Preprocessed Data": "https://raw.githubusercontent.com/yashhackz360/Railway_Accdeint_Analytics_A_data_driven_AI_Approach/main/Assests/preprocessed_accident_data.csv", # Assuming CSV
    "Enhanced Data (for AI)": "https://raw.githubusercontent.com/yashhackz360/Railway_Accdeint_Analytics_A_data_driven_AI_Approach/main/Assests/enhanced_accident_data.csv" # Assuming CSV
}


# --- Caching the data loading function ---
@st.cache_data
def load_data(url):
    """Loads data from a URL, handling both CSV and Excel files."""
    try:
        # Added a check for spaces in URL which need to be encoded
        url = url.replace(" ", "%20")
        if url.endswith('.csv'):
            return pd.read_csv(url)
        elif url.endswith('.xlsx'):
            return pd.read_excel(url)
    except Exception as e:
        st.error(f"Error loading data from {url}: {e}")
        st.warning("Please ensure the file exists at the specified URL in your GitHub repository and the link is a 'raw' link.")
        return None

# --- App Layout ---

# Header
st.markdown("""
<div style="text-align: center; color: #60A5FA;">
    <h1>🚆 Project Overview</h1>
</div>
""", unsafe_allow_html=True)

# --- Dataset Selection and Display ---
st.subheader("📄 Explore the Project Datasets")
selected_dataset_name = st.selectbox(
    "Choose a dataset to preview:",
    options=list(DATASETS.keys())
)

selected_url = DATASETS[selected_dataset_name]
df = load_data(selected_url)

if df is not None:
    st.success(f"✅ Previewing **{selected_dataset_name}**.")
    st.dataframe(df.head())
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=f"📥 Download {selected_dataset_name} as CSV",
        data=csv,
        file_name=f"{selected_dataset_name.replace(' ', '_').lower()}.csv",
        mime='text/csv',
    )


# ---------- Styling ----------
st.markdown("""
<style>
    .section-heading {
        font-size: 20px;
        font-weight: bold;
        color: #ff5733;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Project Description Sections ----------
st.write("""
This project leverages data analytics, machine learning, and AI to enhance railway safety in India. By analyzing historical data and applying predictive modeling, it aims to provide actionable insights for accident prevention and maintenance.
""")

# 📊 Power BI Dashboard
st.markdown('<div class="section-heading">📊 Power BI Dashboard</div>', unsafe_allow_html=True)
st.write("""
A **Power BI dashboard** provides an interactive visual representation of accident trends and safety metrics.
""")
st.info("ℹ️ **Dataset Used:** `Uncleaned_railway_accident_1900_2024.xlsx` is the primary source for the dashboard, allowing for a complete overview of the raw data.")


# 🐍 EDA Section
st.markdown('<div class="section-heading">🐍 Insights and Analysis</div>', unsafe_allow_html=True)
st.write("""
Comprehensive exploratory data analysis (EDA) of railway accident data to uncover patterns and critical risk factors.
""")
st.info("ℹ️ **Dataset Used:** `train_accident_analysis dataset` is used for this section, as it contains the features and aggregations specifically created for deep analysis.")


# 🔮 Predictive Model
st.markdown('<div class="section-heading">🔮 Predictive Model</div>', unsafe_allow_html=True)
st.write("""
Machine learning-powered system that predicts railway accident severity and estimates emergency response needs.
""")
st.info("ℹ️ **Dataset Used:** `preprocessed_accident_data` is used to train and evaluate the predictive models, as it has been cleaned, scaled, and prepared for machine learning algorithms.")


# 🤖 AI Chatbot
st.markdown('<div class="section-heading">🤖 AI Chatbot</div>', unsafe_allow_html=True)
st.write("""
An AI-powered chatbot that provides real-time answers and insights into railway safety, trends, and recommendations.
""")
st.info("ℹ️ **Dataset Used:** `enhanced_accident_data` powers the chatbot, providing it with a rich, context-aware knowledge base for answering user queries accurately.")
