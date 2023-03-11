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
graph_styles = ['bar','line','area','scatter']
sel_col = st.multiselect('Select a month to Visualize', columns)
sel_graph = st.sidebar.radio("Select a graph style to visualize",graph_styles)

if sel_graph == graph_styles[0]:
    fig = px.bar(df, x=df.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)
if sel_graph == graph_styles[1]:
    fig = px.line(df, x=df.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)
if sel_graph == graph_styles[2]:
    fig = px.area(df, x=df.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)
if sel_graph == graph_styles[3]:
    fig = px.scatter(df, x=df.index, y=sel_col)
    st.plotly_chart(fig, use_container_width=True)

