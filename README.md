# Railway Accident Analytics Platform

## Overview

This project provides a comprehensive platform for analyzing railway accident data, predicting accident severity, estimating resource requirements, and offering AI-driven insights. The platform integrates historical data analysis, predictive modeling using machine learning, and an AI assistant powered by LLaMA for intelligent query handling.

## Features

-   **Data Visualization**: Interactive dashboards created with Streamlit and Power BI for exploring accident trends, causes, and impacts.
-   **Predictive Modeling**: Utilizes a Random Forest Regressor to predict accident severity based on key features.
-   **AI Assistant**: Uses LLaMA to answer questions about the dataset.
-   **Resource Estimation**: Estimates required ambulances and structural damage costs based on accident parameters.

## Technologies Used

-   Streamlit
-   Pandas
-   Scikit-learn
-   Matplotlib
-   Seaborn
-   Power BI (optional for advanced visualization)
-   Groq API (for LLaMA integration)


## Modules

-   **Home Overview**: Provides a project introduction and navigation links.
-   **Insights and Analysis**: Explores historical accident data, visualizes trends, and identifies key factors.
-   **Power BI Report**: Integrates interactive dashboards created with Power BI for in-depth data exploration.
-   **Predictive Model**: Deploys a machine learning model to predict accident severity and estimate resource needs.
-   **AI Assistant**: Uses LLaMA for intelligent query handling.

## Data Sources

-   **Historical Accident Data**: `"train_accident_analysis-dataset.csv"` contains accident records and is used for historical analysis.
-   **Enhanced Accident Data**: `"enhanced_accident_data.csv"` includes processed features for predictive modeling.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

