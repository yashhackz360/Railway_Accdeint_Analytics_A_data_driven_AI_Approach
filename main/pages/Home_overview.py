import streamlit as st


def show():
    st.markdown(
   """
    <div style="text-align: center; color: #60A5FA;">
    <h1>🚆 Project Overview</h1>
    </div>
    """,
    unsafe_allow_html=True
)
    # Instructions to the user
    st.write(" Download the dataset by clicking the button below. ")
    # Provide the absolute path to the file
    csv_path = r"C:/Users/yashw/Desktop/6 th sem project ideas/train_Accident_1900_2024_cleaned.xlsx"

    try:
        # Attempt to open 
        with open(csv_path, "rb") as csv:
            st.download_button(
                label="Download the Dataset",
                data=csv,
                file_name="Indian_Railways_Accidents_Dataset_1902_2024.xlsx",  # Corrected file name
            )
    except FileNotFoundError:
        # Display an error if the file is not found
        st.error(f"The file was not found at the specified location: {csv_path}")
    except Exception as e:
        # Handle any other errors
        st.error(f"An unexpected error occurred: {e}")

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

    # Project Overview
    

    st.write("""
   This project leverages data analytics, machine learning, and AI to enhance railway safety in India. By analyzing historical data and applying predictive modeling, it aims to provide actionable insights for accident prevention and  maintenance.
    """)

    # Power BI Dashboard
    st.markdown('<div class="section-heading">📊 Power BI Dashboard</div>', unsafe_allow_html=True)
    st.write("""
    A **Power BI dashboard** provides an **interactive visual representation** of accident trends, financial expenditures, and rescue response times. **Key features include:**
    """)
    st.markdown("""
    ✅ **Historical accident trends** 📈 over the decades.\n  
    ✅ **Accident hotspots** 📍 across different states. \n 
    ✅ **Impact of funding allocations** 💰 on accident reduction. \n 
    ✅ **Rescue response efficiency** ⏱️ and its role in mitigating damage.  
    """)
    
   # Exploratory Data Analysis (EDA) Section
    st.markdown('<div class="section-heading">🐍Insights and Analysis</div>', unsafe_allow_html=True)
    st.write("""
    This section provides a **comprehensive exploratory data analysis (EDA)** of railway accident data, uncovering key patterns and trends to better understand contributing factors.
    """)
    st.markdown("""
    ✅ **Data Upload & Preview** – Users can upload railway accident data (CSV) and preview its structure.  
    ✅ **Preprocessing & Categorization** – Converts timestamps, classifies accidents by time of day, season, region, and train type.  
    ✅ **Question-Driven Insights** – Analyzes accident trends based on predefined queries (time, season, location, environment, train type).  
    ✅ **Visual Analytics** – Generates bar plots to highlight key accident trends, aiding in quick pattern recognition.  
    """)
   # Accident Severity Prediction Section
    st.markdown('<div class="section-heading">🔮 Predictive Model: Railway Accident Severity & Resource Estimation</div>', unsafe_allow_html=True)
    st.write("""
    A **machine learning-powered system** that predicts railway accident severity using key factors such as accident type, deaths, injuries, and rescue time.  
    It also estimates required ambulances and structural damage costs to aid response and impact assessment.
    """)
    st.markdown("""
    ✅ **Severity Prediction** – Uses **Random Forest regression** to estimate accident severity.  
    ✅ **Risk Categorization** – Classifies accidents into **Very Low, Low-Level, Mid-Level, or Critical** severity levels.  
    ✅ **Resource Estimation** – Calculates **ambulances required** via a transparent weighted formula.  
    ✅ **Damage Cost Estimation** – Estimates **structural damage costs** based on severity and accident type.  
    ✅ **Interactive UI** – Built with **Streamlit** featuring real-time predictions and clear mathematical explanations.  
    ✅ **Model Metrics** – Displays **MAE and R²** for model performance transparency.  
""")

    
    # AI Chatbot Section
    st.markdown('<div class="section-heading">🤖 AI Chatbot</div>', unsafe_allow_html=True)
    st.write("""
    To enhance accessibility, an **AI-powered chatbot** has been developed to provide **real-time insights** and answer user queries on railway safety.
    """)
    st.markdown("""
    ✅ **Querying accident trends** based on location and year.  
    ✅ **Providing safety recommendations** based on historical data.  
    ✅ **Offering real-time insights** into ongoing railway safety initiatives.  
    """)
     