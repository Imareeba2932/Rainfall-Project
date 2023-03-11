from unicodedata import name
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

st.sidebar.title('ALL INDIA RAINFALL ANALYSIS AND VISUALIZATION')

df = load_dataset()

columns = df.columns.tolist()
groups = ['50Y','25Y','10Y','5Y','2Y']
stats = ['mean','sum','max','min','std']
graph_styles = ['pie','bar','line','area','scatter','histogram']
sel_col = st.multiselect('Select a month to Visualize', columns, default=columns[-1])
sel_graph = st.sidebar.radio("Select a graph style to visualize",graph_styles)
group = st.radio("Select a distribution size",groups, horizontal=True)
stat = st.radio("Select a statistic",stats, horizontal=True)

if stat == stats[0]:
    sdf = df.resample(group).mean()
if stat == stats[1]:
    sdf = df.resample(group).sum()
if stat == stats[2]:
    sdf = df.resample(group).min()
if stat == stats[3]:
    sdf = df.resample(group).max()
if stat == stats[4]:
    sdf = df.resample(group).std()
if sel_graph == graph_styles[1]:
    fig = px.bar(sdf, x=sdf.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)
if sel_graph == graph_styles[2]:
    fig = px.line(sdf, x=sdf.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)
if sel_graph == graph_styles[3]:
    fig = px.area(sdf, x=sdf.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)
if sel_graph == graph_styles[4]:
    fig = px.scatter(sdf, x=sdf.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)
if sel_graph == graph_styles[5]:
    fig = px.histogram(sdf, x=sdf.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)
if sel_graph == graph_styles[0]:
    for col in sel_col:
        fig,ax = plt.subplots(figsize=(7,7))
        sdf[col].plot(kind='pie', ax=ax, title='yearly distribution', autopct='%.1f%%', legend=False)
        st.pyplot(fig)
        