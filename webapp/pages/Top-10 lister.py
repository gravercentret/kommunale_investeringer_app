import streamlit as st
import pandas as pd
import polars as pl
from io import BytesIO
from sqlalchemy import create_engine
import base64
import os
import sys
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

# Function to load and inject CSS into the Streamlit app
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("webapp/style.css")

st.title("Top 10")

col1, col2 = st.columns([0.3, 0.7])
with col1:
    search_query = st.text_input("Søg i tabellen:", "")

filtered_df = st.session_state.df_pl.filter(st.session_state.df_pl["Problematisk ifølge:"].is_not_null())

filtered_df = filter_df_by_search(filtered_df, search_query)

filtered_df = fix_column_types_and_sort(filtered_df)

# Function to filter for 'Alkohol' and get value counts and sum for 'Kommune'
def get_top_kommune_alcohol(filtered_df, top_n=10):
    kommune_summary = (
        filtered_df.group_by('Kommune')
        .agg([
            pl.sum('Markedsværdi (DKK)').alias('Total Markedsværdi (DKK)'),
            pl.len().alias('Antal investeringer')
        ])
        .sort('Total Markedsværdi (DKK)', descending=True)
    )
    # Display the dataframe below the three columns
    display_df = kommune_summary.with_columns(
        pl.col('Total Markedsværdi (DKK)')
        .map_elements(round_to_million, return_dtype=pl.Utf8)
        .alias('Total Markedsværdi (DKK)'),
    )
    return display_df.head(top_n)

# Streamlit app
if search_query:
    st.subheader(f"Top 10 for '{search_query}':")
else: 
    st.subheader("Kommuner med flest problematiske investeringer:")

# Get top 10 municipalities for 'Alkohol'
top_10_kommune = get_top_kommune_alcohol(filtered_df)

# Display the result in the Streamlit app
st.write("Top 10 kommuner med den største sum af problematiske investeringer:")
st.dataframe(top_10_kommune)