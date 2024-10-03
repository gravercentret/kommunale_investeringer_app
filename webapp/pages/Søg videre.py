import streamlit as st
import polars as pl
import base64
import os
from utils.data_processing import (
    get_data,
    decrypt_dataframe,
    filter_df_by_search,
    fix_column_types_and_sort,
    format_number_european,
    get_unique_categories,
    filter_dataframe_by_category,
)
from config import set_pandas_options, set_streamlit_options

# Apply the settings
set_pandas_options()
set_streamlit_options()


# Function to load and inject CSS into the Streamlit app
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("webapp/style.css")

if "df_pl" not in st.session_state:
    with st.spinner("Henter data..."):
        df_retrieved = get_data()
        encoded_key = os.getenv("ENCRYPTION_KEY")

        if not encoded_key:
            raise ValueError("ENCRYPTION_KEY is not set in the environment variables.")

        encryption_key = base64.b64decode(encoded_key)
        col_list = ["Kommune", "ISIN kode", "Værdipapirets navn"]
        st.session_state.df_pl = decrypt_dataframe(df_retrieved, encryption_key, col_list)

st.title("Søg videre i databasen")
st.subheader("Se top 10 baseret på din søgning og filtrering.")
col1, col2 = st.columns([0.4, 0.6])

# Multiselect defaults
default_priorities = [2, 3]
unique_categories_list = get_unique_categories(st.session_state.df_pl)

with col1:
    search_query = st.text_input("Søg i tabellen:", "")
    selected_priorities = st.multiselect(
        "Vælg prioritet:",
        options=[None, 1, 2, 3],
        default=default_priorities,
        format_func=lambda x: {None: "Resten", 1: "Gul", 2: "Orange", 3: "Rød"}.get(x, str(x)),
    )
    selected_categories = st.multiselect(
        "Vælg årsag(er):",
        unique_categories_list,
        help="Vælg én eller flere årsager at filtrere efter.",
        placeholder="Vælg årsagskategorier."
    )

with col2:
    with st.container(border=True):
        st.markdown("""
            ### Sådan bruger du søgeværktøjet:
            - **Sprogforskelle:** Søgeværktøjet skelner mellem forskellige sprog. For eksempel vil en søgning på 'Kina' ikke give resultater for 'China'. Sørg derfor for at prøve flere varianter af søgeord.
            - **Eksperimentér med søgeord:** Hvis du ikke finder det, du leder efter med det samme, så prøv forskellige formuleringer eller delord af det, du søger.
            - **Download data:** Ønsker du at downloade filtrerede data? Brug download-ikonet, som findes øverst i tabellen.
            """)

# Filter the dataframe by selected priorities and search query
filtered_df = st.session_state.df_pl.filter(
    (st.session_state.df_pl["Priority"].is_in([p for p in selected_priorities if p is not None])) |
    (st.session_state.df_pl["Priority"].is_null())
) if None in selected_priorities else st.session_state.df_pl.filter(
    st.session_state.df_pl["Priority"].is_in(selected_priorities)
)

filtered_df = filter_df_by_search(filtered_df, search_query)
filtered_df = filter_dataframe_by_category(filtered_df, selected_categories)
filtered_df = fix_column_types_and_sort(filtered_df)


# Function to get top 10 municipalities based on market value or count
def get_top_10(filtered_df, group_by_col, sort_by_col, top_n=10):
    kommune_summary = (
        filtered_df.group_by("Kommune")
        .agg([
            pl.len().alias("Antal investeringer"),
            pl.sum("Markedsværdi (DKK)").alias("Total Markedsværdi (DKK)")
        ])
        .sort(sort_by_col, descending=True)
    )
    return kommune_summary.with_columns(
        pl.col("Total Markedsværdi (DKK)").map_elements(format_number_european, return_dtype=pl.Utf8)
    ).head(top_n)

# Display search results
st.subheader(f"Top 10 for '{search_query}':" if search_query else "Kommuner med flest problematiske investeringer:")
st.markdown(
    f"***Antal kommuner/regioner{' med' if not search_query else ' hvor'} '{search_query or 'problematisk investering'}' indgår:*** \n **{filtered_df.select(pl.col('Kommune').n_unique()).to_numpy()[0][0]}**"
)

# Display top 10 based on sum and count
col_sum, col_count = st.columns(2)

with col_sum:
    top_10_sum = get_top_10(filtered_df, "Kommune", "Total Markedsværdi (DKK)")
    st.write("Top 10 kommuner med den største sum:")
    st.dataframe(top_10_sum)

with col_count:
    top_10_count = get_top_10(filtered_df, "Kommune", "Antal investeringer")
    st.write("Top 10 kommuner med det største antal af investeringer:")
    st.dataframe(top_10_count)

# Display the filtered dataframe
st.write("Data for alle:")
st.dataframe(filtered_df)