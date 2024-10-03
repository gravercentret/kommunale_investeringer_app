import streamlit as st
from config import set_pandas_options, set_streamlit_options
import uuid
from datetime import datetime

# Generate or retrieve session ID
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = str(uuid.uuid4())  # Generate a unique ID

# Get the current timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Log the user session with a print statement
user_id = st.session_state['user_id']
print(f"[{timestamp}] New user session: {user_id} (Mulige kilder)")

st.logo("webapp/images/GC_png_oneline_lockup_Outline_Blaa_RGB.png")

# Apply the settings
set_pandas_options()
set_streamlit_options()

st.title("Citater til fri afbenyttelse")

st.subheader("Noget om at vi har fået nogle citater, der kan bruges")

st.markdown(
    """
Hverken KL eller Danske Regioner ønsker at komme med nogle råd eller anbefalinger til deres medlemmer vedrørende investeringer.

KL er kommet med følgende skriftlige kommentar: "KL yder ikke finansiel rådgivning til kommunerne, så vi har ikke råd og anbefalinger ift. kommunernes placering af midler. Det er op til kommunerne inden for styrelseslovens rammer."

Og Danske Regioner svarer følgende: "Det er ikke noget Danske Regioner rådgiver om."
"""
)
