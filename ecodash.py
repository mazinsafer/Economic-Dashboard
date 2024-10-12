# import streamlit as st
# import streamlit.components.v1 as components

# st.title("U.S. Economic Dashboard")

# # Use components.html for embedding with custom sizes
# components.html(
#     """
#     <iframe title="FinancialMap" width="100%" height="1200" 
#     src="https://app.powerbi.com/view?r=eyJrIjoiYTUyMzJjZjQtMWZiMi00NTRhLTg5MzYtZDRlOTZmNTFkNWExIiwidCI6IjE3MGJiYWJkLWEyZjAtNGM5MC1hZDRiLTBlOGYwZjBjNDI1OSIsImMiOjN9" 
#     frameborder="0" allowFullScreen="true"></iframe>
#     """,
#     width=1500,  # Set this to a larger width to make the iframe wider
#     height=1200  # Set height to make the iframe taller
# )

import streamlit as st
import streamlit.components.v1 as components

# Make Streamlit page take the full screen width
st.set_page_config(layout="wide")

st.title("U.S. Economic Dashboard")

# Center the iframe and make it slightly larger
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






