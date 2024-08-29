import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import geojson
import plotly.io as pio

st.set_page_config(layout="wide")

pio.templates.default = "plotly"

# st.write('''
# # Example of a Data Dashboard
# - interactive data table 
# - seaborn plots with filters 
# - plotly plot
# ''')

tab1, tab2, tab3 = st.tabs(["Trends in Registered Passenger Cars", "Changes by County", "Top Manufacturer"])

with tab1:
# 1st plot
    st.header('Number of Registered Passenger Cars by Fuel Type as of January 1st Each Year')

    df = pd.read_excel('./data/other/car_stock_2014-2024.xlsx')

    fig = px.bar(df, 
                x="Year", 
                y=["Petrol", 'Diesel','Hybrid','BEV','LPG','CNG','others'],
                labels={'value':'Number of Cars','variable':'Fuel Types'},
                height = 700,
                #  color='variable',
                #  title='Number of Registered Passenger Cars Grouped by Fuels Type in Germany on January 1st',
                )
    fig.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)
    st.plotly_chart(fig)


with tab2:
    # 2nd plot
    st.header('Change in the Number of Registered Cars by County, 2018-2024')

    with open('./kreise-germany.geojson', 'r') as file:
        geojson_data = geojson.load(file)

    df_registered_cars = pd.read_csv('./data/other/registered_cars_per_county_2018-2024.csv', sep=';')

    fuel_type = st.radio('Select fuel type', ['Total','Petrol','Diesel','BEV','Hybrid','Gas','Others'], index=3, horizontal=True, key='ozgsd')
    color_dict = {'Total':[20000,250000],'Petrol':[20000,150000],'Diesel':[10000,100000],'Gas':[100,4000],'Hybrid':[600,20000],'BEV':[150,10000],'Others':[0,100]}

    fig2 = px.choropleth_mapbox(data_frame = df_registered_cars, 
                                locations='county',
                                color=fuel_type,
                                range_color=color_dict[fuel_type],
                                geojson=geojson_data, 
                                featureidkey='properties.krs_name', # Check out the GeoJSON file (we loaded it as geojson_data)...
                                opacity=0.8,
                                zoom=5.2, 
                                center={'lat': 51.163361, 'lon': 10.447683}, # use Nominatim from geopy.geocoders to find your center
                                animation_frame= 'year',
                                # animation_group= 'county',
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


    st.header('Number of EVs per 1000 Residents by County')
    
    fig3 = px.choropleth_mapbox(data_frame = df_registered_cars, 
                                locations='county',
                                color='ev_1000',
                                labels={'ev_1000':'Number of EVs per 1000 Residents'},
                                range_color=[10,90],
                                geojson=geojson_data, 
                                featureidkey='properties.krs_name', # Check out the GeoJSON file (we loaded it as geojson_data)...
                                opacity=0.6,
                                zoom=5.2, 
                                center={'lat': 51.163361, 'lon': 10.447683}, # use Nominatim from geopy.geocoders to find your center
                                animation_frame= 'year',
                                mapbox_style='carto-positron',
                                color_continuous_scale = 'reds',
                                height=900,
                                # width=900
                                )
    fig3.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)
    st.plotly_chart(fig3)




with tab3:
    # 3rd plot
    st.header('Number of Registered Passenger Cars by Manufacturer on January 1, 2024')


    df_by_manufacturer = pd.read_excel('./data/other/registered_car_by_manufacturer.xlsx')

    fuel_type = st.radio('Select fuel type', ['Total','Petrol','Diesel','BEV','Hybrid','Others'], index=3, horizontal = True, key='ssgtret')

    if fuel_type == 'Total':
        fuel = ['Petrol', 'Diesel', 'BEV', 'Hybrid', 'Others']
    else:
        fuel = fuel_type


    fig4 = px.bar(df_by_manufacturer.sort_values(fuel_type, ascending=False), 
                x="Manufacturer", 
                y=fuel,
                labels={'value':'Number of Registered Cars','variable':'Fuel Types'},
                height = 700,
                #  text='value',
                # title='Top 10 Manufacturers in Germany (Number of cars on 01.01.2024)',
                )

    fig4.update_layout(xaxis = go.layout.XAxis(tickangle = 45))
    fig4.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)

    st.plotly_chart(fig4)
