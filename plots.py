# Core Pkg
import streamlit as st

# Load EDA Pkgs
import pandas as pd
import numpy as np

# Load plotly Data Viz Pkgs
# from streamlit_folium import folium_static
# import leafmap.foliumap as leafmap
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def count_hist(df,x, y): # Returns Plotly Histogram Figure
    fig = px.histogram(df, 
                    x=x, 
                    y=y,
                    # title=f"{la} - Incidents",
                    # width=1000,
                    # height=800,
                    # labels={"unique_values": "", "count": "Counts"},
                    template='simple_white',
                    )
    # Title
    fig.update_layout(
        title_x=0.5,
        title_xanchor='center',
        # title_pad_l=500,
        title_font=dict(
            size = 40,     
        )
    )
    # Y-axes
    fig.update_yaxes(
    showgrid=True,
    automargin=True
    )
    # X-axes
    fig.update_xaxes(
        tickangle=45, 
        tickfont=dict(
            family='Rockwell', 
            color='crimson', 
            size=14),
            type="category",
            automargin=True)


    #Layout
    fig.update_layout(
    autosize=False,
    # width=900,
    height=800,
    font=dict(
        family="Courier New, monospace",
        size=15,
        color="white"
        )
    )
    return fig

def map_it(df, x, y):
                    
    fig = go.Figure()
    layout = dict(
    geo_scope='usa',
    )

    fig.add_trace(
    go.Choropleth(
            locations=df[x],
            zmax=1,
            z = df[y],
            locationmode = 'USA-states', 
            marker_line_color='white',
            geo='geo',
            colorscale=px.colors.sequential.Teal, 
    )
    )

    fig.update_layout(layout)  
    return fig


def count_hist_custom(df,x, y, label): # Returns Plotly Histogram Figure
    fig = px.histogram(df, 
                    x=x, 
                    y=y,
                    # title=f"{title}",
                    # width=1000,
                    # height=800,
                    labels={x: label[0], y: label[1]},
                    template='simple_white',
                    )
    # Title
    fig.update_layout(
        title_x=0.5,
        title_xanchor='center',
        # title_pad_l=500,
        title_font=dict(
            size = 40,     
        )
    )
    # Y-axes
    fig.update_yaxes(
    showgrid=True,
    automargin=True
    )
    # X-axes
    fig.update_xaxes(
        tickangle=45, 
        tickfont=dict(
            family='Rockwell', 
            color='crimson', 
            size=14),
            type="category",
            automargin=True)


    #Layout
    fig.update_layout(
    autosize=False,
    # width=900,
    height=800,
    font=dict(
        family="Courier New, monospace",
        size=15,
        color="white"
        )
    )

    return fig