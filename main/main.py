import streamlit as st
from streamlit_option_menu import option_menu
from pages import Home_overview
from pages import Insights_and_Analysis
from pages import Power_BI_Report
from pages import Predictive_Model
from pages import llama_Assitant

# Page config
st.set_page_config(page_title="yash's Railway Accident Analytics platform", layout="wide", initial_sidebar_state="collapsed")

# Main title & its CSS styling
st.markdown(
"""
<style>
/* Centering the title */
.title-container {
text-align: center;
padding: 20px;
}

/* Stylish gradient text effect */
.title-container h1 {
font-size: 2.8rem;
font-weight: bold;
background: linear-gradient(90deg, #ff8c00, #ff2e63); /* Vibrant warm tones */
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}
</style>

<div class="title-container">
<h1>Railway Accident Analytics : A Data-Driven AI Approach</h1>
</div>
""",
unsafe_allow_html=True
)

# Overall styling
st.markdown(
"""
<style>
/* Background gradient */
.stApp {
background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
height: 100vh;
display: flex;
justify-content: center;
align-items: center;
color: white;
}

/* Enhancing button look */
.stButton>button {
background-color: #ff7e5f; /* Modern warm contrast */
color: white;
border-radius: 8px;
padding: 10px 20px;
font-size: 16px;
font-weight: bold;
transition: 0.3s;
}

/* Button hover effect */
.stButton>button:hover {
background-color: #feb47b;
transform: scale(1.05);
}
</style>
""",
unsafe_allow_html=True
)

# Navigation
menu = ["Home", "Power BI Report", "Insights and Analysis", "Predictive Model", "AI Assistant"]
icons = ["house", "bar-chart", "graph-up", "cpu", "robot"]

# Horizontal navigation menu
selected_section = option_menu(
menu_title="", # No title to keep it compact
options=menu,
icons=icons,
menu_icon="cast",
default_index=0,
orientation="horizontal"
)

# Page routing
if selected_section == "Home":
 Home_overview.show()
elif selected_section == "Power BI Report":
 Power_BI_Report.show()
elif selected_section == "Insights and Analysis":
 Insights_and_Analysis.show()
elif selected_section == "Predictive Model":
 Predictive_Model.show()
elif selected_section == "AI Assistant":
 llama_Assitant.show()