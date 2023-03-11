import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

@st.cache
def load_dataset():
    df=pd.read_csv('datasets/All-India-Rainfall-Act_Dep_1901_to_2019_0.csv')
    df.rename({'JUN-SEP':'ALL'}, axis=1, inplace=True)
    df.YEAR = pd.to_datetime(df.YEAR, format='%Y')
    df.set_index('YEAR', inplace=True)
    return df

st.sidebar.title('Month wise analysis')

df = load_dataset()

columns = df.columns.tolist()
sel_col = st.sidebar.radio('Select a month to Visualize', columns)
st.subheader(f'You have selected {sel_col}')
fig=px.histogram(df, x=sel_col)
fig=px.density_contour(df,x=sel_col)
fig2=px.histogram(df, x=sel_col)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig, use_container_width=True)
