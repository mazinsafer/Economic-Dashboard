import streamlit as st
import streamlit.components.v1 as components

st.title("U.S. Economic Dashboard")


st.markdown(
    """
    <iframe width="100%" height="1000" src="<iframe title="FinancialMap (1)" width="800" height="836" src="https://app.powerbi.com/view?r=eyJrIjoiYTUyMzJjZjQtMWZiMi00NTRhLTg5MzYtZDRlOTZmNTFkNWExIiwidCI6IjE3MGJiYWJkLWEyZjAtNGM5MC1hZDRiLTBlOGYwZjBjNDI1OSIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>" frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True
)

components.html(
    """
    <iframe title="U.S. Economic Dashboard" width="1000" height="1000" src="https://app.powerbi.com/view?r=YOUR_REPORT_ID" frameborder="0" allowFullScreen="true"></iframe>
    """,
    width=1000,
    height=1000,
)


