import polars as pl
import plotly.express as px
import streamlit as st
from utils.data_processing import (
    round_to_million,
    format_number_european
)


def create_pie_chart(filtered_df):
    # Group the data by 'Type' and sum the 'Markedsværdi (DKK)'
    type_distribution = (
        filtered_df.group_by("Type")
        .agg(pl.col("Markedsværdi (DKK)").sum().alias("Total Markedsværdi"))
        .to_pandas()
    )  # Convert to pandas for plotting

    # Drop rows with missing values (NaN) in 'Total Markedsværdi' or 'Type'
    type_distribution = type_distribution.dropna(subset=["Total Markedsværdi", "Type"])

    # Combine 'Andet' and 'Ikke angivet' into one category
    type_distribution["Type"] = type_distribution["Type"].replace(
        {"Andet": "Andet/ikke angivet", "Ikke angivet": "Andet/ikke angivet"}
    )

    # Re-aggregate the data to group by the combined category, summing only the numeric column
    type_distribution = type_distribution.groupby("Type", as_index=False)[
        "Total Markedsværdi"
    ].sum()

    # Define a color mapping for consistent colors
    color_mapping = {
        "Aktie": "cornflowerblue",
        "Obligation": "lightgreen",
        "Virksomhedsobligation": "lightblue",
        "Andet/Ikke angivet": "lightgray",
    }

    # Match the colors with the values in 'Type'
    type_distribution["color"] = type_distribution["Type"].map(color_mapping)

    # Apply rounding to 'Total Markedsværdi' for display in hover text
    type_distribution["Markedsværdi_display"] = type_distribution["Total Markedsværdi"].apply(
        lambda x: format_number_european(x, 0)  # Format with European conventions
    )

    total_value = type_distribution["Total Markedsværdi"].sum()
    type_distribution["Percent"] = type_distribution["Total Markedsværdi"].apply(
        lambda x: f"{format_number_european((x / total_value) * 100, 2)} %" 
    )

    # Combine Markedsværdi_display and Percent into one hover text string
    type_distribution["Hover_text"] = type_distribution.apply(
        lambda row: f"{row['Markedsværdi_display']} ({row['Percent']})", axis=1
    )

    # Create a pie chart using Plotly
    fig = px.pie(
        type_distribution,
        values="Total Markedsværdi",
        names="Type",
        color="Type",  # Set colors for categories
        color_discrete_map=color_mapping,
        title="Fordeling af investeringer (DKK)",
    )
    
    fig.update_traces(
        textinfo="percent",  # Show only percentage
        texttemplate="%{percent:.0%}",  # Rounded percentage, no decimals
        hovertemplate="<b>%{label}</b><br>Markedsværdi DKK (andel): %{customdata[0]}<br>",  
        customdata=type_distribution[["Hover_text"]].to_numpy(), 
        sort=False,  # Keeps the original order of the data
        rotation=90
    )


    # Adjust the layout to prevent text from being cut off
    fig.update_layout(
        title=dict(
            font=dict(size=20),
        ),
        showlegend=True,
        legend_title="Type",
        legend=dict(
            x=1,  # Adjusts horizontal position of the legend
            y=1,  # Adjusts vertical position of the legend
            traceorder="normal",
            font=dict(size=14),
            bgcolor="rgba(0,0,0,0)",  # Transparent background
        ),
        margin=dict(l=50, r=150, t=50, b=50),  # Increase right margin for legend
    )
    #fig.layout.yaxis.tickformat = ',.0%'

    st.plotly_chart(fig)
