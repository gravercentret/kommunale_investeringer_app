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

st.header("Citater til fri afbenyttelse")

st.markdown(
    " ###### Følgende citater er til fri afbenyttelse i forbindelse med omtale af informationer fra dette datasæt:"
)

st.markdown(
    """
Hverken KL eller Danske Regioner ønsker at komme med nogle råd eller anbefalinger til deres medlemmer vedrørende investeringer.

KL er kommet med følgende skriftlige kommentar: "KL yder ikke finansiel rådgivning til kommunerne, så vi har ikke råd og anbefalinger ift. kommunernes placering af midler. Det er op til kommunerne inden for styrelseslovens rammer."

Og Danske Regioner svarer følgende: "Det er ikke noget Danske Regioner rådgiver om."
"""
)

st.header("Mulige kilder")

st.markdown(
    """
            De oplagte kilder til historier på baggrund af data er naturligvis kommunen eller regionen selv. 
            Det vil typisk være de politiske valgte, der vil være mest interessante at tale med, 
            for der er ikke noget ulovligt i at investere i problematiske værdipapirer. Det er mere et spørgsmål om moral og etik.\n
I kommunerne vil det være borgmesteren, der er født formand for økonomiudvalget og repræsentanter for oppositionen i kommunen, 
            der vil være interessante at få en kommentar fra.\n
Det samme gør sig gældende for regionerne.\n
Det kunne også være interessant at tale med presseafdelingerne for de banker og pensionskasser, 
            der havde sortlistet nogle bestemte papirer for at få en uddybning af årsagen til eksklusionen.\n
"""
)
