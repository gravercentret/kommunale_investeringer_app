import streamlit as st
from config import set_pandas_options, set_streamlit_options
from utils.data_processing import load_css, write_markdown_sidebar, create_user_session_log

create_user_session_log("Reglerne på området")

# Apply the settings
set_pandas_options()
set_streamlit_options()

load_css("webapp/style.css")
st.logo("webapp/images/GC_png_oneline_lockup_Outline_Blaa_RGB.png")

with st.sidebar:
    write_markdown_sidebar()

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
