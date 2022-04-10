import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout='wide')

df = px.data.gapminder()




st.title('Welcome to the Streamlit Dashboard!')

conti = st.sidebar.selectbox("Please select one continent: ", ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania'])

fig = px.scatter(df.query('continent==@conti'), x="gdpPercap", y="lifeExp", size="pop", color="country", hover_name="country", log_x=True, size_max=60,animation_frame='year',range_y=[20,100])

st.plotly_chart(fig,use_container_width=True)

