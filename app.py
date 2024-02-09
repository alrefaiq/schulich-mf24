# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:30:52 2024

@author: qusay
"""

import streamlit as st
import pandas as pd
import plotly.express as px

#Grab Data
df = pd.read_csv('StockData/AAPL.csv', parse_dates=['Date'], index_col=['Date'])

#create charts
fig = px.line(df, y='Adj Close')
#Outputs
st.title("DEMO APP - Schulich Class")
st.write(df) #similar to print but it will show in the app
st.plotly_chart(fig) #output plotly graph

#in the console type: !streamlit run app.py