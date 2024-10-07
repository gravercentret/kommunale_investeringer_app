import streamlit as st
import uuid
from datetime import datetime
from config import set_pandas_options, set_streamlit_options
from utils.data_processing import load_css, write_markdown_sidebar

# Generate or retrieve session ID
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())  # Generate a unique ID

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log the user session with a print statement
user_id = st.session_state["user_id"]
print(f"[{timestamp}] New user session: {user_id} (Mulige kilder)")

st.logo("webapp/images/GC_png_oneline_lockup_Outline_Blaa_RGB.png")

# Apply the settings
set_pandas_options()
set_streamlit_options()
load_css("webapp/style.css")

with st.sidebar:
    write_markdown_sidebar()

st.header("Klausulering og kildeangivelse")
# Overordnede afsnit
st.markdown(
    """
            Al information på dette site er klausuleret til den 21. oktober kl. 6.00 \n
            Hvis der anvendes data fra denne database i et journalistisk produkt eller i en anden sammenhæng, skal Gravercentret og Danwatch nævnes som kilde. \n
For eksempel kan du skrive: "Det viser data, som er indsamlet og bearbejdet af Gravercentret - Danmarks Center for Undersøgende Journalistik, i samarbejde med Danwatch."\n
"""
)
