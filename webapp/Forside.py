import streamlit as st
import pandas as pd
import polars as pl
from io import BytesIO
from sqlalchemy import create_engine
import base64
import os
import sys
# from dotenv import load_dotenv  # Required if using .env file
# from streamlit_extras.stylable_container import stylable_container
from utils.data_processing import (
    get_data,
    decrypt_dataframe,
    get_unique_kommuner,
    filter_dataframe_by_choice,
    generate_organization_links,
    filter_df_by_search,
    fix_column_types_and_sort,
    format_number_european,
    round_to_million,
    get_ai_text,
)
from utils.plots import create_pie_chart
from config import set_pandas_options, set_streamlit_options

# Apply the settings
set_pandas_options()
set_streamlit_options()

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Function to load and inject CSS into the Streamlit app
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("webapp/style.css")


if "df_pl" not in st.session_state:
    with st.spinner("Henter data..."):
        df_retrieved = get_data()
        # Optional: load environment variables from the .env file
        # load_dotenv()

        encoded_key = os.getenv("ENCRYPTION_KEY")

        if encoded_key is None:
            raise ValueError("ENCRYPTION_KEY is not set in the environment variables.")

        encryption_key = base64.b64decode(encoded_key)

        col_list = ["Kommune", "ISIN kode", "Værdipapirets navn"]
        st.session_state.df_pl = decrypt_dataframe(df_retrieved, encryption_key, col_list)

st.logo("webapp/images/GC_navnetraek_Lille_Blaa_RGB.png")

# Title of the app
st.title("Kommunale og regionale investeringer")

st.markdown(
    """
            Gravercentret har sammen med Danwatch undersøgt, hvilke værdipapirer de danske kommuner og regioner har valgt at investere i. \n
            Disse oplysninger har vi sammenholdt med lister over hvilke værdipapirer, der er sortlistet af danske banker og pensionsselskaber samt FN. 
            Herunder kan du se oplysninger fra alle kommuner og regioner - og du kan downloade oplysningerne i Excel-format.
            """
)
with st.expander("Læs mere: Hvordan skal tallene forstås?", icon="❔"):
    st.markdown("""
                For hvert værdipapir er det angivet, hvilken kommune eller region, der er ejeren, hvad værdipapirets navn er og hvad værdien af positionen er.\n
                Værdipapirer, der er udpeget som problematiske, vil være markeret med enten en rød, en orange eller en gul firkant.\n
                - 🟥 **Rød**: Disse værdipapirer er udstedt af problematiske selskaber.
                - 🟧 **Orange**: Disse værdipapirer er udstedet af problematiske lande.
                - 🟨 **Gul**: Disse værdipapirer er potentielt kontroversielle.\n
                For hvert værdipapir, der er markeret enten med rød, orange eller gul vil der være en forklaring på, hvem, der har udpeget det som problematisk og hvad årsagen er.\n
                Endelig kan man se, hvilke type værdipapiret er (typisk om det er en aktie eller en obligation), ISIN-nummeret (som er et unikt nummer ligesom et CPR-nummer) samt hvem, der har udstedt papiret.\n
                Data kan downloades til Excel nedenfor tabellen.\n
                """)
# Get unique municipalities and sort alphabetically
unique_kommuner = get_unique_kommuner(st.session_state.df_pl)

# Define custom categories
all_values = "Hele landet"
municipalities = "Alle kommuner"
regions = "Alle regioner"
samsø = "Samsø"
læsø = "Læsø"

# Combine Samsø, Læsø with unique_kommuner and sort alphabetically
sorted_kommuner = sorted(unique_kommuner + [samsø, læsø])
# Create dropdown options
dropdown_options = [all_values, municipalities, regions] + unique_kommuner

# Sidebar with selection options
with st.sidebar:
    user_choice = st.selectbox(
        "Vælg område:",
        dropdown_options,
        help="Skriv i boksen for at søge efter bestemt kommune/region.",
        placeholder="Vælg en kommune/region.",
    )

    search_query = st.text_input("Søg i tabellen:", "")

    # Filter dataframe based on user's selection
    filtered_df = filter_dataframe_by_choice(st.session_state.df_pl, user_choice)

    filtered_df = filter_df_by_search(filtered_df, search_query)

    filtered_df = fix_column_types_and_sort(filtered_df)

    if user_choice in [all_values, municipalities, regions] and search_query:
        st.markdown(f"Antal kommuner/regioner, hvor '{search_query}' indgår: \n **{filtered_df.select(pl.col("Kommune").n_unique()).to_numpy()[0][0]}**")

    st.header("Sådan gjorde vi")
    st.markdown(
        """
        Noget om, at vi har søgt aktindsigt.
        """
    )


# Conditionally display the header based on whether a search query is provided
if search_query:
    st.header(f'Data for "{user_choice}" og "{search_query}":')
else:
    st.header(f'Data for "{user_choice}":')

if filtered_df.shape[0] == 0:
    st.subheader(f"**{user_choice} har oplyst, at den ikke har nogen investeringer.**")


# Create three columns
col1, col2 = st.columns([0.4, 0.6])

# Assuming filtered_df is your Polars dataframe that has been filtered already
# Column 1: Pie chart for "Type" based on "Markedsværdi (DKK)"
with col1:

    create_pie_chart(filtered_df)

# Column 2: Number of problematic investments
with col2:
    with st.container(border=True):
        col2_1, col2_2, col2_3 = st.columns(3)
        height_col = 180

        with col2_1:
            with st.container(border=True, height=height_col):
                st.markdown("***Antal investeringer udpeget som problematiske:***")

                # Count the rows where 'Problematisk ifølge:' is not empty
                problematic_count_red = filtered_df.filter(filtered_df["Priority"] == 3).shape[0]

                # Display the number in red
                st.markdown(
                    f'<h1 style="color:red;">{problematic_count_red}</h1>', unsafe_allow_html=True
                )
        with col2_2:
            with st.container(border=True, height=height_col):
                st.markdown("***Antal investeringer fra ekskluderede lande:***")
                problematic_count_orange = filtered_df.filter(filtered_df["Priority"] == 2).shape[0]

                # Display the second number in yellow
                st.markdown(
                    f'<h1 style="color:#FE6E34;">{problematic_count_orange}</h1>',
                    unsafe_allow_html=True,
                )
        with col2_3:
            with st.container(border=True, height=height_col):
                st.markdown("***Antal investeringer værd at undersøge nærmere:***")

                problematic_count_yellow = filtered_df.filter(filtered_df["Priority"] == 1).shape[0]

                # Display the second number in yellow
                st.markdown(
                    f'<h1 style="color:#FEB342;">{problematic_count_yellow}</h1>',
                    unsafe_allow_html=True,
                )
    # Nøgletal
    with st.container(border=True):
        st.subheader("Nøgletal")

        # Calculate the total number of investments
        antal_inv = len(filtered_df)
        st.write(f"**Antal investeringer:** {antal_inv}")

        # Calculate the total sum of 'Markedsværdi (DKK)' and display it in both DKK and millions
        total_markedsvaerdi = (
            filtered_df.select(pl.sum("Markedsværdi (DKK)")).to_pandas().iloc[0, 0]
        ).astype(int)

        markedsvaerdi_million = round_to_million(total_markedsvaerdi)
        st.write(
            f"**Total Markedsværdi (DKK):** {markedsvaerdi_million}"  # {total_markedsvaerdi:,.2f}
        )

        # Filter for problematic investments and calculate the total sum of their 'Markedsværdi (DKK)'
        prob_df = filtered_df.filter(filtered_df["Problematisk ifølge:"].is_not_null())
        prob_markedsvaerdi = (
            prob_df.select(pl.sum("Markedsværdi (DKK)")).to_pandas().iloc[0, 0]
        ).astype(int)

        prob_markedsvaerdi_million = round_to_million(prob_markedsvaerdi)
        st.write(
            f"**Markedsværdi af problematiske investeringer:** {prob_markedsvaerdi_million}"  # {prob_markedsvaerdi:,.2f}
        )


# Display the dataframe below the three columns
display_df = filtered_df.with_columns(
    pl.col("Markedsværdi (DKK)")
    .map_elements(format_number_european, return_dtype=pl.Utf8)
    .alias("Markedsværdi (DKK)"),
)


def enlarge_emoji(val):
    return f'<span style="font-size:24px;">{val}</span>'


st.dataframe(
    display_df[
        [
            # "Index",
            "OBS",
            "Kommune",
            "Værdipapirets navn",
            "Markedsværdi (DKK)",
            # "Problematisk ifølge:",
            "Årsag til eksklusion",
            "Type",
            "ISIN kode",
            "Udsteder",
        ]
    ],
    column_config={
        "OBS": st.column_config.TextColumn(),
        "Kommune": "Kommune",
        "Udsteder": st.column_config.TextColumn(width="small"),
        "Markedsværdi (DKK)": "Markedsværdi (DKK)",  # st.column_config.NumberColumn(format="%.2f"),
        "Type": "Type",
        "Problematisk ifølge:": st.column_config.TextColumn(width="medium"),
        "Årsag til eksklusion": st.column_config.TextColumn(
            width="large", help="Årsagen er taget fra eksklusionslisterne."
        ),  # 1200
        "Udsteder": st.column_config.TextColumn(width="large"),
    },
    hide_index=True,
)

# Call the function to display relevant links based on the 'Problematisk ifølge:' column
generate_organization_links(filtered_df, "Problematisk ifølge:")


# Function to convert dataframe to Excel and create a downloadable file
def to_excel(filtered_df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        filtered_df.to_excel(writer, index=False)
    processed_data = output.getvalue()
    return processed_data


filtered_df = filtered_df.to_pandas()
filtered_df.drop("Priority", axis=1, inplace=True)
# Convert dataframe to Excel
excel_data = to_excel(filtered_df)

# Create a download button
st.download_button(
    label="Download til Excel",
    data=excel_data,
    file_name=f"Investeringer for {user_choice}{search_query}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)

if user_choice not in [all_values, municipalities, regions, samsø, læsø]:
    st.subheader(f"Eksklusionsårsager for investeringer foretaget af {user_choice}: ")

    ai_text = get_ai_text(user_choice)

    st.markdown(ai_text)

    st.info(
        """Eksklusionslisten ovenfor er genereret med kunstig intelligens, og der tages derfor forbehold for fejl.
        Overstående liste er muligvis ikke udtømmende, det er tilfældig udvalgte eksempler.""",
        icon="ℹ️",
    )
