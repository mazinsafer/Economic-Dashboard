import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("U.S. Economic Dashboard")


components.html(
    """
    <div style="display: flex; justify-content: center;">
        <iframe title="FinancialMap" width="90%" height="1300" 
        src="https://app.powerbi.com/view?r=eyJrIjoiYTUyMzJjZjQtMWZiMi00NTRhLTg5MzYtZDRlOTZmNTFkNWExIiwidCI6IjE3MGJiYWJkLWEyZjAtNGM5MC1hZDRiLTBlOGYwZjBjNDI1OSIsImMiOjN9" 
        frameborder="0" allowFullScreen="true"></iframe>
    </div>
    """,
    height=1300
)






