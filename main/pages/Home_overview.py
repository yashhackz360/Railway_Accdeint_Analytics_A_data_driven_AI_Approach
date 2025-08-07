import streamlit as st
import pandas as pd
import os

# Set page title
st.set_page_config(page_title="Railway Accident Analytics - Overview", layout="wide")

# Load dataset from 'Assests' directory
dataset_path = os.path.join("..", "main", "Assests", "train_Accident_1900_2024_cleaned.csv")


# Header
st.markdown("""
<div style="text-align: center; color: #60A5FA;">
    <h1>🚆 Project Overview</h1>
</div>
""", unsafe_allow_html=True)

# Try to load dataset
try:
    df = pd.read_csv(dataset_path)

    # ✅ Success message
    st.success("✅ Dataset loaded successfully.")

    # 📊 Dataset overview
    st.subheader("📄 Dataset Overview")
    st.write(f"**Total Rows:** {df.shape[0]}")
    st.write(f"**Total Columns:** {df.shape[1]}")
    st.dataframe(df.head())  # Show top 5 rows

    # 📥 Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name='train_Accident_1900_2024_cleaned.csv',
        mime='text/csv',
    )

except FileNotFoundError:
    st.error("❌ Dataset file not found. Please check the path.")
except Exception as e:
    st.error(f"❌ Error loading dataset: {e}")

# ---------- Styling ----------
st.markdown("""
<style>
    .title-section {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #007bff;
        margin-bottom: 10px;
    }
    .section-heading {
        font-size: 20px;
        font-weight: bold;
        color: #ff5733;
        margin-top: 20px;
    }
    .bullet-point {
        margin-left: 20px;
        font-size: 16px;
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
st.markdown("""
✅ **Historical accident trends** 📈 over the decades.  
✅ **Accident hotspots** 📍 across different states.  
✅ **Impact of funding allocations** 💰 on accident reduction.  
✅ **Rescue response efficiency** ⏱️ and its role in mitigating damage.  
""")

# 🐍 EDA Section
st.markdown('<div class="section-heading">🐍 Insights and Analysis</div>', unsafe_allow_html=True)
st.write("""
Comprehensive exploratory data analysis (EDA) of railway accident data to uncover patterns and critical risk factors.
""")

# 🔮 Predictive Model
st.markdown('<div class="section-heading">🔮 Predictive Model</div>', unsafe_allow_html=True)
st.write("""
Machine learning-powered system that predicts railway accident severity and estimates emergency response needs.
""")

# 🤖 AI Chatbot
st.markdown('<div class="section-heading">🤖 AI Chatbot</div>', unsafe_allow_html=True)
st.write("""
An AI-powered chatbot that provides real-time answers and insights into railway safety, trends, and recommendations.
""")
