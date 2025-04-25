import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.markdown(
       """
        <div style="text-align: center; color: #60A5FA;">
            <h1>📈 Python EDA </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Enhanced CSS Styling
    st.markdown(
        """
        <style>
            .question { font-size: 18px; font-weight: bold; text-align: left; color: #333333; padding: 8px; border-radius: 5px; margin-bottom: 8px; background-color: #f0f2f6; }
            .answer { font-size: 14px; text-align: left; color: #2e4053; padding: 8px; border: 1px solid #cccccc; border-radius: 5px; margin-bottom: 12px; background-color: #ffffff; }
            .plot-title { font-size: 16px; font-weight: bold; text-align: center; color: #2e4053; margin-bottom: 8px; }
        </style>
        """, unsafe_allow_html=True)

    # File Upload
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Dataset Preview")
        st.write(df.head())

        # Data Preprocessing
        df['time'] = pd.to_datetime(df['time'], errors='coerce')
        df.dropna(subset=['time'], inplace=True)  # Remove rows with invalid dates
        df['hour'] = df['time'].dt.hour
        df['daytime'] = pd.cut(df['hour'], [0, 6, 12, 18, 24],
                               labels=["Night", "Morning", "Afternoon", "Evening"])

        seasons = ["Winter" if i.month in [12, 1, 2, 3] else "Summer" if i.month in range(4, 7)
                   else "Monsoon" if i.month in range(7, 10) else "Autumn" for i in df["time"]]
        df["season"] = seasons

        TRAIN_TYPES = ["Express", "Passenger", "Freight", "Mail", "others"]
        df['train_type'] = df['train_name'].apply(
            lambda x: next((t for t in TRAIN_TYPES if t in x), "Unknown"))

        region_map = {"n": "North", "nc": "North", "ne": "North", "nef": "North", "nw": "North",
                      "s": "South", "sc": "South", "se": "South", "sw": "South",
                      "e": "East", "ec": "East", "eco": "East", "c": "Central", "w": "West"}
        df['region'] = df['railway_division'].map(region_map).fillna("Unknown")

        # Remove "Unknown" and "Others" categories
        df = df[df['daytime'] != 'Unknown']
        df = df[df['season'] != 'Unknown']
        df = df[df['region'] != 'Unknown']
        df = df[df['train_type'] != 'Unknown']
        df = df[df['env'] != 'Unknown']
        df = df[df['cause'] != 'unknown']  # Remove unknown causes as well

        # Questions & Analysis
        questions = [
            ("On which time of day do more accidents happen? Does visibility play a major role?", 'daytime'),
            ("In which season are accidents more frequent?", 'season'),
            ("Which region of the country has experienced more accidents?", 'region'),
            ("What is the environment of accident spots (e.g., open area, flood-affected area, or bad track)?", 'env'),
            ("Which type of trains suffer more accidents (express, passenger, freight, etc.)?", 'train_type')
        ]

        for question, col in questions:
            st.write(f"<p class='question'>{question}</p>", unsafe_allow_html=True)

            # Reduced figure size
            fig, ax = plt.subplots(figsize=(8, 4))  # Even smaller plots
            sns.barplot(x=df[col].value_counts().index, y=df[col].value_counts().values, ax=ax, palette='viridis')
            ax.set_xlabel(col.replace('_', ' ').title(), fontsize=10)
            ax.set_ylabel("Accident Count", fontsize=10)
            ax.set_title(question, fontsize=12)
            plt.xticks(rotation=45, ha='right', fontsize=8)  # Smaller x-axis labels
            plt.yticks(fontsize=8)  # Smaller y-axis labels
            plt.tight_layout()  # Adjust layout to prevent labels from overlapping
            st.pyplot(fig)

            # Answer Section with descriptive findings
            most_common = df[col].value_counts().idxmax()
            count = df[col].value_counts().max()
            st.write(
                f"<p class='answer'><b>Finding:</b> Most accidents occur during the <b>{most_common}</b> with <b>{count}</b> occurrences.</p>",
                unsafe_allow_html=True)

            # Additional Descriptive Analysis

            if col == 'daytime':
                st.write("<p class='answer'>Accidents during night and early morning may be linked to reduced visibility. Further investigation into lighting conditions and safety protocols during these times is recommended.</p>", unsafe_allow_html=True)
            elif col == 'season':
                st.write("<p class='answer'>Accidents in certain seasons may be due to weather conditions (monsoon, winter fog). Evaluate weather-related safety protocols and infrastructure resilience.</p>", unsafe_allow_html=True)
            elif col == 'region':
                st.write("<p class='answer'>Specific regional challenges (terrain, infrastructure) may contribute to higher accident rates. Targeted safety improvements and resource allocation may be necessary.</p>", unsafe_allow_html=True)
            elif col == 'env':
                st.write("<p class='answer'>Understanding the environment of accident spots can highlight risks such as unmanned crossings or track conditions. Focused safety measures are needed for these areas.</p>", unsafe_allow_html=True)
            elif col == 'train_type':
                st.write("<p class='answer'>Accidents involving particular train types may point to operational or maintenance issues. Review safety protocols and maintenance schedules for these trains.</p>", unsafe_allow_html=True)

        # --- Additional Analysis: Casualties by Region ---
        st.write(f"<p class='question'>What are the casualties (injured and killed) by region?</p>", unsafe_allow_html=True)
        region_casualties = df.groupby('region')[['injured', 'killed']].sum()
        st.write(region_casualties)

        # Reduced size
        fig_casualties, ax_casualties = plt.subplots(figsize=(8, 4)) # Even smaller plots
        region_casualties.plot(kind='bar', ax=ax_casualties, colormap='coolwarm')
        ax_casualties.set_xlabel("Region", fontsize=10)
        ax_casualties.set_ylabel("Number of People", fontsize=10)
        ax_casualties.set_title("Casualties (Injured and Killed) by Region", fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=8)
        plt.yticks(fontsize=8)
        plt.tight_layout()
        st.pyplot(fig_casualties)

        # --- Additional Analysis: Causes of Accidents ---
        st.write(f"<p class='question'>What are the main causes of accidents?</p>", unsafe_allow_html=True)
        cause_counts = df['cause'].value_counts()
        # Reduced size
        fig_cause, ax_cause = plt.subplots(figsize=(8, 4))  # Even smaller plots
        sns.barplot(x=cause_counts.index, y=cause_counts.values, ax=ax_cause, palette='magma')
        ax_cause.set_xlabel("Cause", fontsize=10)
        ax_cause.set_ylabel("Number of Accidents", fontsize=10)
        ax_cause.set_title("Accident Counts by Cause", fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=8)
        plt.yticks(fontsize=8)
        plt.tight_layout()
        st.pyplot(fig_cause)
        st.write(f"<p class='answer'>The most frequent cause of accidents is: <b>{cause_counts.idxmax()}</b> with <b>{cause_counts.max()}</b> occurrences.</p>", unsafe_allow_html=True)

        # Conclusion
        st.write("### Conclusion")
        st.write("Some accidents can be prevented through better safety measures, while others, such as those caused by extreme weather, are harder to mitigate.")
        st.write("Human negligence remains a major factor in accidents, requiring increased awareness and training for train operators and the public.")

        # Limitations
        st.write("### Limitations of This Data")
        st.write("- Some accidents are not well-documented due to brief reports in news sources.")
        st.write("- The dataset does not cover external attacks or the condition of trains in detail.")
        st.write("- This report focuses on accident counts from 2002-2017 but provides some analysis of casualties.")
    else:
        st.info("Upload  railway accdeint data to perform Exploaratory Data Analysis.")


if __name__ == "__main__":
    st.write("This should be run as a module and not a script")
