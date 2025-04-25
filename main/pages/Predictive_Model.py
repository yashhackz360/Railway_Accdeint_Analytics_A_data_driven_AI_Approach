import streamlit as st
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, r2_score

# --- Constants ---
FEATURES = ['Standard Accident Type', 'Deaths', 'Injuries', 'Rescue Time (hrs)']
TARGET_SEVERITY = 'Severity'

# Severity classification thresholds
CRITICAL_THRESHOLD = 75
MID_LEVEL_THRESHOLD = 50
LOW_LEVEL_THRESHOLD = 25


@st.cache_data
def load_data(uploaded_file):
    """Load CSV data and store original dataframe in session state."""
    try:
        df = pd.read_csv(uploaded_file)
        st.session_state.original_df = df.copy()
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None


def preprocess_data(df):
    """Calculate severity, encode categorical features, and scale numericals."""
    df = df.copy()

    # Calculate severity if not present
    if TARGET_SEVERITY not in df.columns:
        df[TARGET_SEVERITY] = df['Deaths'] + df['Injuries']

    categorical_features = ['Standard Accident Type']
    numerical_features = ['Deaths', 'Injuries', 'Rescue Time (hrs)']

    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer([
        ('num', numeric_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

    X = df[FEATURES]
    X_processed = preprocessor.fit_transform(X)

    st.session_state.preprocessor = preprocessor
    st.session_state.feature_names = preprocessor.get_feature_names_out()

    return pd.DataFrame(X_processed, columns=st.session_state.feature_names), df[TARGET_SEVERITY]


def train_severity_model(X, y):
    """Train Random Forest regression model and store metrics."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.session_state.severity_model = model
    st.session_state.severity_mae = mae
    st.session_state.severity_r2 = r2


def classify_severity(score):
    """Classify severity score into descriptive levels."""
    if score >= CRITICAL_THRESHOLD:
        return "Critical"
    elif score >= MID_LEVEL_THRESHOLD:
        return "Mid-Level"
    elif score >= LOW_LEVEL_THRESHOLD:
        return "Low-Level"
    else:
        return "Very Low"


def estimate_ambulances(deaths, injuries, rescue_time):
    """
    Estimate ambulances needed:
    ceil((Deaths * 0.3) + (Injuries * 0.5) + (Rescue Time (hrs) * 0.8))
    """
    ambulances = math.ceil((deaths * 0.3) + (injuries * 0.5) + (rescue_time * 0.8))
    if ambulances == 0 and (deaths > 0 or injuries > 0 or rescue_time > 0):
        ambulances = 1
    return ambulances


def estimate_structural_damage_cost(accident_type, deaths, injuries):
    """
    Estimate structural damage cost (INR) based on accident type and severity.
    """
    base_costs = {
        'Bombing': 100_000_000,
        'Fire': 70_000_000,
        'Derailment': 50_000_000,
        'Collision': 30_000_000,
        'Other': 20_000_000
    }
    base_cost = base_costs.get(accident_type, base_costs['Other'])
    severity_score = deaths + injuries

    if severity_score >= 100:
        multiplier = 2.0
    elif 50 <= severity_score < 100:
        multiplier = 1.5
    elif 25 <= severity_score < 50:
        multiplier = 1.2
    else:
        multiplier = 1.0

    return base_cost * multiplier


def show():
    """Main Streamlit UI function."""
    
    st.markdown(
       """
        <div style="text-align: center; color: #60A5FA;">
            <h1> 🔮 Railway Accident Severity Analytics </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("Upload your accident data CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if df is not None:
            st.subheader("Raw Data Preview")
            st.dataframe(df.head())

            X_processed, y = preprocess_data(df)

            st.subheader("Preprocessed Feature Sample")
            st.dataframe(X_processed.head())

            if st.button("Train Severity Prediction Model"):
                train_severity_model(X_processed, y)
                st.success(f"Severity Model Trained! MAE: {st.session_state.severity_mae:.2f}, R²: {st.session_state.severity_r2:.2f}")

    if ('severity_model' in st.session_state and
        'preprocessor' in st.session_state and
        'feature_names' in st.session_state and
        'original_df' in st.session_state):

        st.markdown("---")
        st.header("Make Predictions")

        accident_types = list(st.session_state.original_df['Standard Accident Type'].unique())
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            accident_type = st.selectbox("Accident Type", accident_types)
        with col2:
            deaths = st.number_input("Number of Deaths", min_value=0, step=1)
        with col3:
            injuries = st.number_input("Number of Injuries", min_value=0, step=1)
        with col4:
            rescue_time = st.number_input("Rescue Time (hrs)", min_value=0, step=1)

        if st.button("Predict Accident Severity and Outcomes"):
            input_df = pd.DataFrame({
                'Standard Accident Type': [accident_type],
                'Deaths': [deaths],
                'Injuries': [injuries],
                'Rescue Time (hrs)': [rescue_time]
            })

            # Preprocess input
            X_input = st.session_state.preprocessor.transform(input_df)
            X_input_df = pd.DataFrame(X_input, columns=st.session_state.feature_names)

            # Predict severity
            severity_pred = st.session_state.severity_model.predict(X_input_df)[0]
            severity_level = classify_severity(severity_pred)

            # Estimate ambulances
            estimated_ambulances = estimate_ambulances(deaths, injuries, rescue_time)

            # Estimate structural damage cost
            estimated_damage_cost = estimate_structural_damage_cost(accident_type, deaths, injuries)

            # Display results professionally
            st.markdown("## 🚦 Prediction Results")
            col1, col2 = st.columns(2)

            with col1:
                st.metric("Predicted Severity Score", f"{severity_pred:.2f}")
                st.metric("Severity Level", severity_level)
                st.metric("Estimated Ambulances Required", f"{estimated_ambulances}")

            with col2:
                st.metric("Structural Damage Cost (INR)", f"₹{estimated_damage_cost:,.0f}")
                st.markdown("### 📊 Model Performance")
                st.info(f"MAE: {st.session_state.severity_mae:.2f} | R²: {st.session_state.severity_r2:.2f}")

            # Show math behind the model with proper LaTeX rendering
            st.markdown("---")
            st.markdown("### 🧮 Math Behind the Model")

            # Severity score and level math
            st.markdown("**Severity Score Calculation:**")
            st.latex(r"""\text{Severity Score (Input)} = \text{Deaths} + \text{Injuries}""")

            st.markdown("**Model Prediction:**")
            st.latex(r"""\text{Predicted Severity Score} = f(\text{Accident Type},\, \text{Deaths},\, \text{Injuries},\, \text{Rescue Time (hrs)})""")

            st.markdown("**Severity Level Assignment:**")
            st.latex(r"""
            \begin{cases}
            \text{Critical}, & \text{if } \text{Predicted Severity Score} \geq 75 \\
            \text{Mid-Level}, & \text{if } 50 \leq \text{Predicted Severity Score} < 75 \\
            \text{Low-Level}, & \text{if } 25 \leq \text{Predicted Severity Score} < 50 \\
            \text{Very Low}, & \text{if } \text{Predicted Severity Score} < 25
            \end{cases}
            """)

            # Ambulance estimation formula
            st.markdown("**Ambulance Estimation Formula:**")
            st.latex(r"""\text{Estimated Ambulances} = \left\lceil 
            (\text{Deaths} \times 0.3) + (\text{Injuries} \times 0.5) + (\text{Rescue Time (hrs)} \times 0.8)
            \right\rceil""")

            # Structural damage cost formula
            st.markdown("**Structural Damage Cost:**")
            st.markdown("""
            **Base Cost by Accident Type:**

            - Bombing: ₹1,00,00,000  
            - Fire: ₹70,00,000  
            - Derailment: ₹50,00,000  
            - Collision: ₹30,00,000  
            - Other: ₹20,00,000  
            """)

            st.markdown("**Severity Multiplier:**")

            st.markdown("""
            - ≥ 100: ×2.0  
            - 50–99: ×1.5  
            - 25–49: ×1.2  
            - < 25: ×1.0  
            """)

            st.markdown("**Total Cost:**")
            st.latex(r"""\text{Estimated Cost} = \text{Base Cost} \times \text{Multiplier}""")

    else:
        st.info("Upload data and train the severity model to enable predictions.")


if __name__ == "__main__":
    show()
