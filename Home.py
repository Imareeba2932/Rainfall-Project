import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt


st.image("assets/img.png", use_column_width=True)

st.subheader('ABOUT')
st.markdown('''
Rianfall is one of the climatological data which is widely analyzed for a long time. Rainfall is a prime input for various engineering design such as hydraulic structures, sewer and road drainage system, bridges and canals etc.
The detailed statistical analysis of rainfall data is essential as it facilitates policy decisions reegarding the cropping pattern, sowing date, construction of roads and providing drinking water to urban and rural areas. Statistical
analyses are carried out to determine the rainfall event intensity for specific return periods.

This analysis will provide useful information for water resources planner, farmers and urban engineers to assess the availability of water and create storage accordingly. 
''')