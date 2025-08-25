import streamlit as st
import pandas as pd

def show():
    """
    This function encapsulates the entire content of the Home/Overview page.
    It is called by the main app script to display this page.
    """

    # --- Dataset Loading from Google Drive ---

    # This dictionary now uses the direct download links for your Google Drive files.
    DATASETS = {
        "Main Cleaned Data (XLSX)": "https://docs.google.com/spreadsheets/d/1OHSMfrEbKBrBkuPkAUaGj2AZBTyhCbKO/export?format=xlsx",
        "Enhanced Data (for AI)": "https://drive.google.com/uc?export=download&id=1-o-0UdR5gCQ74R5B_ZjqThp2FeobRFo7",
        "Analysis Dataset": "https://drive.google.com/uc?export=download&id=1FV7E_UifZJ3EMY8XjT3t__Q8YNqGH11c"
        # Note: I've removed the other two datasets as links were not provided. You can add them back if needed.
    }

    # --- Caching the data loading function ---
    @st.cache_data
    def load_data(url, name):
        """Loads data from a URL, handling both CSV and Excel files."""
        try:
            # The logic is simplified: if the name contains XLSX, use read_excel, otherwise use read_csv.
            if 'XLSX' in name:
                # This requires the 'openpyxl' library to be in requirements.txt
                return pd.read_excel(url)
            else:
                return pd.read_csv(url)
        except Exception as e:
            st.error(f"Error loading data from Google Drive: {e}")
            st.warning("Please ensure the 'Share' setting for each file in Google Drive is set to 'Anyone with the link'.")
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
    # Pass both the URL and the name to the loading function
    df = load_data(selected_url, selected_dataset_name)

    if df is not None:
        st.success(f"✅ Previewing **{selected_dataset_name}** from Google Drive.")
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
    st.info("ℹ️ **Dataset Used:** `Main Cleaned Data (XLSX)` is the primary source for the dashboard, allowing for a complete overview of the raw data.")

    # 🐍 EDA Section
    st.markdown('<div class="section-heading">🐍 Insights and Analysis</div>', unsafe_allow_html=True)
    st.write("""
    Comprehensive exploratory data analysis (EDA) of railway accident data to uncover patterns and critical risk factors.
    """)
    st.info("ℹ️ **Dataset Used:** `Analysis Dataset` is used for this section, as it contains the features and aggregations specifically created for deep analysis.")

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
    st.info("ℹ️ **Dataset Used:** `Enhanced Data (for AI)` powers the chatbot, providing it with a rich, context-aware knowledge base for answering user queries accurately.")

# This block allows you to run this page's script directly for testing
if __name__ == "__main__":
    st.set_page_config(page_title="Railway Accident Analytics - Overview", layout="wide")
    show()
