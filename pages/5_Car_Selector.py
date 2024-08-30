import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import geojson
import plotly.io as pio

st.set_page_config(layout="wide")

pio.templates.default = "plotly"

df = pd.read_csv('./data/auto_all_final.csv', sep=';', parse_dates=['First registration'])
df_bev = df[df['engine_type'] == 'BEV']

st.header('Car Selector')

# select brand
brand_list = st.multiselect('Select your brand',
                        df_bev['brand'].unique()
                        )
brand_mask = df_bev['brand'].isin(brand_list)
if brand_list == []:
    data = df_bev
else:
    data = df_bev[brand_mask]

# select model
if brand_list != []:
    model_list = st.multiselect('Select your model',
                                df_bev[brand_mask]['model'].unique()
                                )
    model_mask = df_bev['model'].isin(model_list)
    if model_list == []:
        data = df_bev[brand_mask]
    else:
        data = df_bev[model_mask]

fig3 = px.scatter(data,
                x='First registration',
                y='price',
                size='Mileage',
                color='brand',
                labels={'brand':'Brand','price':'Price'},
                hover_data=['brand','model'],
                size_max=30,
                height=800,
                opacity=1
                )

fig3.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)


st.plotly_chart(fig3)

