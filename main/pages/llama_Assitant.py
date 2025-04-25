import pandas as pd
import streamlit as st
import requests

def show():
    # ✅ API Setup (For general safety queries only)
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    GROQ_API_KEY = "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"  # Replace with your actual API key

    # ✅ Load Railway Accident Data
    @st.cache_data
    def load_data():
        try:
            df = pd.read_csv("C:/Users/yashw/Desktop/6 th sem project ideas/Indian_Railways_Accidents_Dataset_1902_2024.csv")
            return df
        except FileNotFoundError:
            st.error("⚠️ Railway accident dataset not found!")
            return None

    df = load_data()

    # ✅ Query Functions for Dataset
    def get_accident_stats():
        """Returns general statistics from the dataset."""
        return df.describe().to_string() if df is not None else "No data available."

    def get_accidents_by_cause(cause):
        """Returns accidents related to a specific cause."""
        if df is not None:
            filtered_data = df[df["Cause"].str.contains(cause, case=False, na=False)]
            return filtered_data.to_string(index=False) if not filtered_data.empty else "No records found."
        return "No data available."

    def get_accidents_by_state(state):
        """Returns accidents that occurred in a specific state."""
        if df is not None:
            filtered_data = df[df["State"].str.contains(state, case=False, na=False)]
            return filtered_data.to_string(index=False) if not filtered_data.empty else "No records found."
        return "No data available."

    def get_accidents_by_year(year):
        """Returns accidents that occurred in a specific year."""
        if df is not None:
            filtered_data = df[df["Year"] == int(year)]
            return filtered_data.to_string(index=False) if not filtered_data.empty else "No records found."
        return "No data available."

    # ✅ AI Chat Function (Updated Model)
    def chat_with_ai(prompt):
        # 🔹 Include a summary of the available data in the prompt
        data_summary = f"The available data on Indian railway accidents spans from 1902 to 2024. The model MUST base its answers primarily on this dataset, but can use outside information if required. Do not hallucinate data, instead respond that the data does not exist."
        enhanced_prompt = f"{prompt}. {data_summary}"  # Augment the prompt

        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
        data = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": enhanced_prompt}],
            "max_tokens": 750  # Increased token limit
        }
        response = requests.post(GROQ_API_URL, json=data, headers=headers)
        try:
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"] if "choices" in response_json else f"⚠️ API Error: {response_json}"
        except Exception as e:
            return f"⚠️ Error: {str(e)}"

    # ✅ Streamlit UI
    st.markdown(
       """
        <div style="text-align: center; color: #60A5FA;">
            <h1> 🔍Groq API llama3 Model Chatbot </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("Ask any descriptive details about Indian railway accidents and safety measures!")

    # Chat input
    query = st.text_input("Enter your query:", "")

    if query:
        ai_response = chat_with_ai(query)
        st.write("### AI Response:")
        st.write(ai_response)
