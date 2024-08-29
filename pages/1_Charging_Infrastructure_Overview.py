import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import geojson
import plotly.io as pio

st.set_page_config(layout="wide")

pio.templates.default = "plotly"

tab1, tab2, tab3 = st.tabs(["Growth of Charging Points", "Public Charging Points Development over Time", "Public Charging Points Density Map"])

with tab1:
    # plot 1
    st.header('Change in the Number of Charging Points 2017-2024')

    df= pd.read_excel('./data/other/Charging_points_over_year.xlsx')

    fig = px.bar(df,
                x='Year', 
                y=['Normal Charging Points','Fast Charging Points'], 
                labels={'value':'Number of Charging Points','variable':'Type of Charging Points'},
                opacity = 0.8, 
                barmode='group'
                )
    fig.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)

    st.plotly_chart(fig)

with tab2:
    # plot 2
    st.header('Public Charging Points distribution 2017-2024')

    with open('./kreise-germany.geojson', 'r') as file:
        geojson_data = geojson.load(file)

    df_cp_county = pd.read_csv('./data/other/charging_point_each_county_2017-2024.csv', sep=';')

    charging_type = st.radio('Select charging point type',['Normal Charging Point','Fast Charging Point'], horizontal = True, key='serte')

    fig2 = px.choropleth_mapbox(data_frame = df_cp_county, 
                                locations='County',
                                color=charging_type,
                                range_color=[10,700],
                                geojson=geojson_data, 
                                featureidkey='properties.krs_name', # Check out the GeoJSON file (we loaded it as geojson_data)...
                                opacity=0.8,
                                zoom=5.2, 
                                center={'lat': 51.163361, 'lon': 10.447683}, # use Nominatim from geopy.geocoders to find your center
                                animation_frame= 'Year',
                                animation_group= 'County',
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

with tab3:
    # plot 3
    st.header('Overview of Public Charging Points Distribution in Germany (Stand:16.07.2024)')

    df_charging_station = pd.read_csv('./data/other/charging_station_registry.csv',sep=';')

    fig3 = px.density_mapbox(df_charging_station, 
                            lat='Breitengrad', 
                            lon='Längengrad', 
                            z='Anzahl Ladepunkte', 
                            labels={'Anzahl Ladepunkte':'Number of Charging Points'},
                            radius=10,
                            center=dict(lat=51.163361, lon=10.447683), 
                            zoom=5.2,
                            mapbox_style="carto-positron",
                            height=1000,
                            )
    fig3.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)
    st.plotly_chart(fig3)