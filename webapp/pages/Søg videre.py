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
    to_excel_function,
)
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
print(f"[{timestamp}] New user session: {user_id} (Søg videre)")

# Apply the settings
set_pandas_options()
set_streamlit_options()

st.logo("webapp/images/GC_png_oneline_lockup_Outline_Blaa_RGB.png")

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

with st.sidebar:
    st.header("Ved publicering:")
    st.markdown("""
        Hvis man laver journalistiske historier på baggrund af materialet, skal 
                [Gravercentret](https://www.gravercentret.dk) og [Danwatch](https://danwatch.dk/)\n
        Læs mere om, [hvordan vi har gjort.](/Sådan_har_vi_gjort)""")


st.header("Søg videre i databasen")

default_priorities = [2, 3]
unique_categories_list = get_unique_categories(st.session_state.df_pl)

col1, col2, col3 = st.columns(3)
with col1:
    search_query = st.text_input("Fritekst søgning i data:", "")
with col2:
    selected_priorities = st.multiselect(
        "Vælg type(r):",
        placeholder="Klik for at vælge én eller flere.",
        options=[None, 1, 2, 3],
        default=default_priorities,
        format_func=lambda x: {None: "Øvrige værdipapirer", 1: "Potentielt problematiske", 2: "Problematiske statsobligationer", 3: "Problematiske selskaber"}.get(x, str(x)),
    )
with col3:
    selected_categories = st.multiselect(
        "Vælg problemkategori(er):", 
        unique_categories_list,  # Options
        help="Vi har grupperet de mange årsager til eksklusion i hovedkategorier. Vælg én eller flere.",
        placeholder="Vælg problemkategori."
    )
with st.expander("Om søgeværktøjet", expanded=True):
    st.markdown("""
    #### Sådan bruger du søgeværktøjet:
    Du søger ved først at vælge, hvilke grupper af værdipapirer du vil søge i. 
                    Vi har inddelt dem i fire grupper – værdipapirer fra problematiske selskaber, 
                    statsobligationerne fra problematiske stater, potentielt problematiske papirer og øvrige. 
                    Hvis du vil søge i hele databasen, skal du vælge dem alle til. Vil du blot søge i de problematiske papirer, 
                    så er de to relevante grupper tilføjet fra start som standard.\n
    Herefter kan du fritekstsøge og/eller vælge kategorier af problematiske papirer. Vær opmærksom på:

    - **Sprogforskelle:** Søgeværktøjet skelner mellem forskellige sprog. For eksempel vil en søgning på 'Kina' ikke give resultater for 'China'. Sørg derfor for at prøve flere varianter af søgeord.
    - **Eksperimentér med søgeord:** Hvis du ikke finder det, du leder efter med det samme, så prøv forskellige formuleringer eller delord af det, du søger.
    - **Download data:** Ønsker du at downloade top 10? Brug download-ikonet, som findes øverst i tabellen. I bunden er der en download-knap for det fulde data baseret på de valg, der er taget.
            """
    )

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
def get_top_10(filtered_df, sort_by_col, top_n=10):
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
st.subheader(f"Top 10 for '{search_query}':" if search_query else "Kommuner med flest investeringer:")
st.markdown(
    f"***Antallet af kommuner/regioner:*** \n **{filtered_df.select(pl.col('Kommune').n_unique()).to_numpy()[0][0]}**"
)

# Calculate the sum of all investments in the "Markedsværdi (DKK)" column
investment_sum = filtered_df.select(pl.col('Markedsværdi (DKK)').sum()).to_numpy()[0][0]

# Create the conditional text for the sum
if search_query or selected_categories:
    sum_text = f"***Summen af investeringerne:*** **{format_number_european(investment_sum)} DKK** (Baseret på filtrering)"
else:
    sum_text = f"***Summen af investeringerne:*** **{format_number_european(investment_sum)} DKK**"

# Display the sum with markdown
st.markdown(f"{sum_text}")
# Display top 10 based on sum and count
col_sum, col_count = st.columns(2)

with col_sum:
    top_10_sum = get_top_10(filtered_df, "Total Markedsværdi (DKK)")
    st.write("Top 10 kommuner med den største sum:")
    st.dataframe(top_10_sum)

with col_count:
    top_10_count = get_top_10(filtered_df, "Antal investeringer")
    st.write("Top 10 kommuner med det største antal af investeringer:")
    st.dataframe(top_10_count)

# Display the filtered dataframe
st.write("Data for alle:")

display_df = filtered_df.with_columns(
    pl.col("Markedsværdi (DKK)")
    .map_elements(format_number_european, return_dtype=pl.Utf8)
    .alias("Markedsværdi (DKK)"),
)

st.dataframe(display_df)

filtered_df = display_df.to_pandas()
filtered_df.drop("Priority", axis=1, inplace=True)

# Convert dataframe to Excel
excel_data = to_excel_function(filtered_df)

# Create a download button
st.download_button(
    label="Download til Excel",
    data=excel_data,
    file_name=f"Investeringer-{timestamp}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)