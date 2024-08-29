import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import geojson
import plotly.io as pio

st.set_page_config(layout="wide")

pio.templates.default = "plotly"

tab1, tab2= st.tabs(["Most Offered Brand", "EV Distribution on the Map"])

with tab1:
    st.header('Number of EVs by Brand')
    df = pd.read_csv('./data/auto_all_final.csv', sep=';', parse_dates=['First registration'])
    df_bev = df[df['engine_type'] == 'BEV']

    df_bev_bar = pd.DataFrame(df_bev['brand'].value_counts()).reset_index()

    fig = px.bar(df_bev_bar,
                x='brand', 
                y='count', 
                labels={'brand':'Brand','count':'Number of EVs'},
                opacity = 0.8, 
                barmode='group'
                )
    fig.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)
    st.plotly_chart(fig)


with tab2:
    st.header('Distribution of EVs')
    df_bev_choropleth = pd.DataFrame(df_bev['Kreis name'].value_counts()).reset_index()
    with open('./kreise-germany.geojson', 'r') as file:
        geojson_data = geojson.load(file)

    fig2 = px.choropleth_mapbox(data_frame = df_bev_choropleth, 
                                locations='Kreis name',
                                color='count',
                                labels={'count':'Number of EVs'},
                                range_color=[0,100],
                                geojson=geojson_data, 
                                featureidkey='properties.krs_name', # Check out the GeoJSON file (we loaded it as geojson_data)...
                                opacity=0.8,
                                zoom=5.2, 
                                center={'lat': 51.163361, 'lon': 10.447683}, # use Nominatim from geopy.geocoders to find your center
                                mapbox_style='carto-positron',
                                color_continuous_scale = 'reds',
                                height=900,
                                # width=900
                                )
    fig2.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)
    st.plotly_chart(fig2)
