import streamlit as st
import polars as pl
import base64
import os
from utils.data_processing import (
    get_data,
    decrypt_dataframe,
    filter_df_by_search,
    fix_column_types_and_sort,
    round_to_million,
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
        # Optional: load environment variables from the .env file
        # load_dotenv()

        encoded_key = os.getenv("ENCRYPTION_KEY")

        if encoded_key is None:
            raise ValueError("ENCRYPTION_KEY is not set in the environment variables.")

        encryption_key = base64.b64decode(encoded_key)

        col_list = ["Kommune", "ISIN kode", "Værdipapirets navn"]
        st.session_state.df_pl = decrypt_dataframe(df_retrieved, encryption_key, col_list)

st.title("Top 10")

col1, col2 = st.columns([0.3, 0.7])
# Set default values for the multiselect
default_priorities = [2, 3]

# Create a multiselect widget where users can choose priorities
with col1:
    search_query = st.text_input("Søg i tabellen:", "")

    # Multiselect widget for 'Priority' with default values 2 and 3
    selected_priorities = st.multiselect(
        "Vælg prioritet:",
        options=[None, 1, 2, 3],  # Priority options (None: Almindelig, 1: yellow, 2: orange, 3: red)
        default=default_priorities,
        format_func=lambda x: "Resten" if x is None else {1: "Gul", 2: "Orange", 3: "Rød"}.get(x, str(x))
    )

# Filter the dataframe based on selected priorities
if None in selected_priorities:
    # Handle case where None (null values) are selected
    filtered_df = st.session_state.df_pl.filter(
        (st.session_state.df_pl["Priority"].is_in([p for p in selected_priorities if p is not None])) | 
        (st.session_state.df_pl["Priority"].is_null())
    )
else:
    # Only filter by selected numeric priorities
    filtered_df = st.session_state.df_pl.filter(st.session_state.df_pl["Priority"].is_in(selected_priorities))

filtered_df = filter_df_by_search(filtered_df, search_query)

filtered_df = fix_column_types_and_sort(filtered_df)

# Function to filter for 'Alkohol' and get value counts and sum for 'Kommune'
def get_top_10_sum(filtered_df, top_n=10):
    kommune_summary = (
        filtered_df.group_by('Kommune')
        .agg([
            pl.sum('Markedsværdi (DKK)').alias('Total Markedsværdi (DKK)'),
            pl.len().alias('Antal investeringer')
        ])
        .sort('Total Markedsværdi (DKK)', descending=True)
    )
    # Display the dataframe below the three columns
    display_df_sum = kommune_summary.with_columns(
        pl.col('Total Markedsværdi (DKK)')
        .map_elements(round_to_million, return_dtype=pl.Utf8)
        .alias('Total Markedsværdi (DKK)'),
    )
    return display_df_sum.head(top_n)

# Function to filter for 'Alkohol' and get value counts and sum for 'Kommune'
def get_top_10_count(filtered_df, top_n=10):
    kommune_summary = (
        filtered_df.group_by('Kommune')
        .agg([
            pl.len().alias('Antal investeringer'),
            pl.sum('Markedsværdi (DKK)').alias('Total Markedsværdi (DKK)'),
        ])
        .sort('Antal investeringer', descending=True)
    )
    # Display the dataframe below the three columns
    display_df_count = kommune_summary.with_columns(
        pl.col('Total Markedsværdi (DKK)')
        .map_elements(round_to_million, return_dtype=pl.Utf8)
        .alias('Total Markedsværdi (DKK)'),
    )
    return display_df_count.head(top_n)

# Streamlit app
if search_query:
    st.subheader(f"Top 10 for '{search_query}':")
else: 
    st.subheader("Kommuner med flest problematiske investeringer:")

if search_query:
    st.markdown(f"***Antal kommuner/regioner, hvor '{search_query}' indgår:*** \n **{filtered_df.select(pl.col("Kommune").n_unique()).to_numpy()[0][0]}**")
else: 
    st.markdown(f"***Antal kommuner/regioner med problematiske investeringer:*** \n **{filtered_df.select(pl.col("Kommune").n_unique()).to_numpy()[0][0]}**")


col_sum, col_count = st.columns(2)
with col_sum:
    # Get top 10 municipalities for 'Alkohol'
    top_10_kommune = get_top_10_sum(filtered_df)
    top_10_kommuner_list = top_10_kommune['Kommune'].to_list()

    # Filter the original dataframe based on the top 10 municipalities
    filtered_df_top_10 = filtered_df.filter(pl.col('Kommune').is_in(top_10_kommuner_list))

    # Display the result in the Streamlit app
    st.write("Top 10 kommuner med den største sum af problematiske investeringer:")
    st.dataframe(top_10_kommune)
    
    # Display the result in the Streamlit app
    st.write("Data til grund for top 10:")
    st.dataframe(filtered_df_top_10)


with col_count:
    # Get top 10 municipalities for 'Alkohol'
    top_10_kommune_count = get_top_10_count(filtered_df)
    top_10_kommuner_count_list = top_10_kommune_count['Kommune'].to_list()

    # Filter the original dataframe based on the top 10 municipalities
    filtered_df_top_10_count = filtered_df.filter(pl.col('Kommune').is_in(top_10_kommuner_count_list))

    # Display the result in the Streamlit app
    st.write("Top 10 kommuner med det største antal af problematiske investeringer:")
    st.dataframe(top_10_kommune_count)

    # Display the result in the Streamlit app
    st.write("Data til grund for top 10:")
    st.dataframe(filtered_df_top_10_count)

# Display the result in the Streamlit app
st.write("Data for alle:")
st.dataframe(filtered_df)