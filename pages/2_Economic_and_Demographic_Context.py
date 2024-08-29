import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import geojson
import plotly.io as pio

st.set_page_config(layout="wide")

pio.templates.default = "plotly"

tab1, tab2 = st.tabs(["Disposable Income", "Residents Distribution Map"])

with tab1:
    st.header('Disposable Income of Private Households per Capita in 2021 in 1,000 €')

    with open('./kreise-germany.geojson', 'r') as file:
        geojson_data = geojson.load(file)

    df = pd.read_excel('./data/other/disp_income_pop_density.xlsx')

    fig = px.choropleth_mapbox(data_frame = df, 
                                locations='county',
                                color='disposable_income_2021',
                                range_color=[20,31],
                                labels= {'disposable_income_2021':'Disposable Income in 1,000 €'},
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
    fig.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)
    st.plotly_chart(fig)


with tab2:
    st.header('Residents per km² in 2021')

    fig2 = px.choropleth_mapbox(data_frame = df, 
                                locations='county',
                                color='residents_km2_2021',
                                range_color=[50,800],
                                labels= {'residents_km2_2021':'Residents per km²'},
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
