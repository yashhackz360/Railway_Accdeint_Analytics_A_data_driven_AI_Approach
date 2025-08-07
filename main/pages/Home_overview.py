import streamlit as st
import pandas as pd
import os

def show():
    st.markdown("""
    <div style="text-align: center; color: #60A5FA;">
    <h1>🚆 Project Overview</h1>
    </div>
    """, unsafe_allow_html=True)

    # Correct relative path from 'pages/' to '../Assests/'
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'Assests', 'train_Accident_1900_2024_cleaned.csv')

    try:
        df = pd.read_csv(csv_path)
        st.success("✅ Dataset loaded successfully.")
    except Exception as e:
        st.error(f"❌ Failed to load dataset: {e}")
        return  # Stop further execution if dataset isn't loaded

    # Styling
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

    # ✅ Now continue rendering the page content

    st.write("""
    This project leverages data analytics, machine learning, and AI to enhance railway safety in India. By analyzing historical data and applying predictive modeling, it aims to provide actionable insights for accident prevention and maintenance.
    """)

    # Power BI
    st.markdown('<div class="section-heading">📊 Power BI Dashboard</div>', unsafe_allow_html=True)
    st.write("A **Power BI dashboard** provides an interactive visual representation of accident trends...")

    st.markdown("""
    ✅ **Historical accident trends** 📈 over the decades.  
    ✅ **Accident hotspots** 📍 across different states.  
    ✅ **Impact of funding allocations** 💰 on accident reduction.  
    ✅ **Rescue response efficiency** ⏱️ and its role in mitigating damage.  
    """)

    # EDA
    st.markdown('<div class="section-heading">🐍 Insights and Analysis</div>', unsafe_allow_html=True)
    st.write("Comprehensive exploratory data analysis (EDA) of railway accident data...")

    # Predictive Model
    st.markdown('<div class="section-heading">🔮 Predictive Model</div>', unsafe_allow_html=True)
    st.write("Machine learning-powered system that predicts railway accident severity...")

    # AI Chatbot
    st.markdown('<div class="section-heading">🤖 AI Chatbot</div>', unsafe_allow_html=True)
    st.write("An AI-powered chatbot for real-time safety queries.")
