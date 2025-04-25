import streamlit as st

def show():
    st.markdown(
       """
        <div style="text-align: center; color: #60A5FA;">
            <h1>📊 Power BI Report</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.title("Home Dashboard")
    st.markdown(
            """
            <iframe width="1300" height="650" src="https://app.fabric.microsoft.com/reportEmbed?reportId=895e2ef4-88b6-48e6-a18d-dd9c9bc33392&autoAuth=true&ctid=e09c6192-2b83-4585-8c44-13d4e615579b"></iframe>
            """,
            unsafe_allow_html=True,
        )

    st.title("Casualities & Injuries Section")
    st.markdown(
            """
            <iframe width="1300" height="650" src="https://app.powerbi.com/reportEmbed?reportId=895e2ef4-88b6-48e6-a18d-dd9c9bc33392&autoAuth=true&ctid=e09c6192-2b83-4585-8c44-13d4e615579b"></iframe>
            """,
            unsafe_allow_html=True,
        )
        
    st.title("Geographic Disturbution Section")
    st.markdown(
            """
            <iframe width="1300" height="650" src="https://app.powerbi.com/reportEmbed?reportId=895e2ef4-88b6-48e6-a18d-dd9c9bc33392&autoAuth=true&ctid=e09c6192-2b83-4585-8c44-13d4e615579b"></iframe>
            """,
            unsafe_allow_html=True,
        )
        
    st.title("Top 10 Train Accidents Section")
    st.markdown(
            """
            <iframe width="1300" height="650" src="https://app.powerbi.com/reportEmbed?reportId=895e2ef4-88b6-48e6-a18d-dd9c9bc33392&autoAuth=true&ctid=e09c6192-2b83-4585-8c44-13d4e615579b"></iframe>
            """,
            unsafe_allow_html=True,
        )
