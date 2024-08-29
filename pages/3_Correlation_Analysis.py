import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import geojson
import plotly.io as pio

st.set_page_config(layout="wide")

pio.templates.default = "plotly"


st.header('Correlation Analysis')
df_all = pd.read_excel('./data/other/all_info.xlsx')
data = df_all.drop(['county','lon','lat'], axis=1)
mask = np.triu(np.ones_like(data.corr(), dtype=bool),1)

fig = px.imshow(data.corr().mask(mask),
                x=['Area of the County',
                   'Number of Registered EVs',
                   'Number of Registered EVs per 1000 Residents',
                   'Number of Registered Cars',
                   'Number of Charging Points',
                   'Number of Charging Points per km²',
                   'Number of Charging Points per 1000 Residents',
                   'Disposable Income',
                   'Residents per km²',
                   'Population of the County'
                   ],
                y=['Area of the County',
                   'Number of Registered EVs',
                   'Number of Registered EVs per 1000 Residents',
                   'Number of Registered Cars',
                   'Number of Charging Points',
                   'Number of Charging Points per km²',
                   'Number of Charging Points per 1000 Residents',
                   'Disposable Income',
                   'Residents per km²',
                   'Population of the County'
                   ],
                text_auto='.2f',
                template='simple_white',
                color_continuous_scale='thermal',
                height=800
                )
fig.update_layout(#title_font_size=16,
                   xaxis_title_font_size=20, xaxis_tickfont_size=16,
                   yaxis_title_font_size=20, yaxis_tickfont_size=16,
                   hoverlabel_font_size=16, legend_title_font_size=16,legend_font_size=14)
st.plotly_chart(fig)