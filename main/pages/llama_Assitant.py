import pandas as pd
import streamlit as st
import requests

# ✅ Load AI Chat Assistant Data from Google Drive
# This function should be at the top level (no indentation).
@st.cache_data
def load_data():
    """Loads the enhanced accident data from a public Google Drive link."""
    # Direct download URL for the 'enhanced_accident_data.csv' file
    gdrive_url = "https://drive.google.com/uc?export=download&id=1-o-0UdR5gCQ74R5B_ZjqThp2FeobRFo7"
    try:
        df = pd.read_csv(gdrive_url)
        return df
    except Exception as e:
        st.error(f"⚠️ Error loading data from Google Drive: {e}")
        st.info("Please ensure the file's sharing permission is set to 'Anyone with the link'.")
        return None

# Load the data into a DataFrame at the module level.
df = load_data()

def show():
    """
    This function contains the Streamlit UI and logic for the AI assistant page.
    """
    # ✅ API Setup (For general safety queries only)
    # This now securely loads the API key from Streamlit's secrets management.
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    try:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except KeyError:
        st.error("GROQ_API_KEY not found in Streamlit secrets. Please add it to your secrets file.")
        st.stop()


    # ✅ Query Functions for Dataset
    def get_accident_stats():
        """Returns general statistics from the dataset."""
        return df.describe().to_string() if df is not None else "No data available."

    def get_accidents_by_cause(cause):
        """Returns accidents related to a specific cause."""
        if df is not None:
            filtered_data = df[df["Cause"].str.contains(cause, case=False, na=False)]
            return filtered_data.to_string(index=False) if not filtered_data.empty else "No records found for that cause."
        return "No data available."

    def get_accidents_by_state(state):
        """Returns accidents that occurred in a specific state."""
        if df is not None:
            filtered_data = df[df["State"].str.contains(state, case=False, na=False)]
            return filtered_data.to_string(index=False) if not filtered_data.empty else "No records found for that state."
        return "No data available."

    def get_accidents_by_year(year):
        """Returns accidents that occurred in a specific year."""
        if df is not None:
            try:
                filtered_data = df[df["Year"] == int(year)]
                return filtered_data.to_string(index=False) if not filtered_data.empty else "No records found for that year."
            except (ValueError, TypeError):
                return "Please enter a valid year."
        return "No data available."

    # ✅ AI Chat Function (Updated Model)
    def chat_with_ai(prompt):
        """Sends a prompt to the Groq API and returns the response."""
        data_summary = (
            "The available data on Indian railway accidents spans from 1902 to 2024. "
            "The model MUST base its answers primarily on this dataset, but can use outside information if required. "
            "If the data does not exist for a query, respond that the information is not available in the dataset."
        )
        enhanced_prompt = f"{prompt}. {data_summary}"

        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
        data = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": enhanced_prompt}],
            "max_tokens": 750
        }
        try:
            response = requests.post(GROQ_API_URL, json=data, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"] if "choices" in response_json else f"⚠️ API Error: {response_json}"
        except requests.exceptions.RequestException as e:
            return f"⚠️ Network Error: Could not connect to the API. {e}"
        except Exception as e:
            return f"⚠️ An unexpected error occurred: {str(e)}"

    # ✅ Streamlit UI
    st.markdown(
        """
        <div style="text-align: center; color: #60A5FA;">
            <h1> 🔍 Groq API Llama3 Model Chatbot </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("Ask any descriptive details about Indian railway accidents and safety measures!")

    # Chat input
    query = st.text_input("Enter your query:", "")

    if query:
        with st.spinner("Thinking..."):
            ai_response = chat_with_ai(query)
            st.write("### AI Response:")
            st.write(ai_response)

# To run this page directly for testing
if __name__ == "__main__":
    st.set_page_config(page_title="AI Chat Assistant", layout="wide")
    show()
