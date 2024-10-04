import streamlit as st
from config import set_pandas_options, set_streamlit_options
import uuid
from datetime import datetime
from utils.data_processing import (
    load_css,
)

# Generate or retrieve session ID
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())  # Generate a unique ID

# Get the current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log the user session with a print statement
user_id = st.session_state["user_id"]
print(f"[{timestamp}] New user session: {user_id} (Søg videre)")

# Apply the settings
set_pandas_options()
set_streamlit_options()

load_css("webapp/style.css")
st.logo("webapp/images/GC_png_oneline_lockup_Outline_Blaa_RGB.png")

st.subheader("Sådan er reglerne på området")
st.markdown(
    """
Det er tilladt for kommuner og regioner at investere direkte i stats- 
eller realkreditobligationer eller obligationer, der frembyder en tilsvarende sikkerhed.\n
Men kommuner og regioner må ikke anbringe midler direkte i aktier.\n
Dog kan de anbringe midler i investeringsforeninger, der investerer i 
aktier og dermed eje andele af disse aktier og få del i såvel udbytte som evt. kursstigninger.\n
Det følger af kommunalfuldmagtsreglerne (de uskrevne regler om 
kommunernes opgavevaretagelse), at kommuner som udgangspunkt ikke må 
drive erhvervsvirksomhed, herunder handel, håndværk, industri og finansiel virksomhed, 
medmindre der er lovhjemmel til det.\n
Forbuddet mod at drive kommunal erhvervsvirksomhed er for det første begrundet i, 
at kommunerne har til opgave at udføre opgaver, der kommer almenvellet til gode. 
For det andet er det begrundet i et ønske om at undgå konkurrenceforvridning i 
forhold til den private sektor.\n
**Kilde: Indenrigs- og Sundhedsministeriet**

"""
)
