import streamlit as st

# Title of your Streamlit app
st.title("Power BI Dashboard in Streamlit")

# Embed the Power BI report using an iframe
st.markdown(
    """
    <iframe width="100%" height="800" src="https://app.powerbi.com/view?r=eyJrIjoiOWQxMDlkNDItNGE5MC00YmM2LTgwZDQtYWZkMjIwZTdmOTFhIiwidCI6IjE3MGJiYWJkLWEyZjAtNGM5MC1hZDRiLTBlOGYwZjBjNDI1OSIsImMiOjN9" frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True
)



