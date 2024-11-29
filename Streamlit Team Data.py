#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd

# Load the data from the raw GitHub URL
url = "https://github.com/LeScott2406/TeamData/raw/refs/heads/main/Final.xlsx"
df = pd.read_excel(url)

# Streamlit app
st.title('Football Data Viewer')

# Create the League dropdown filter with "All" as an option
league_options = ['All'] + df['League'].unique().tolist()
selected_league = st.selectbox('Select a League', league_options)

# Filter data based on the selected league
if selected_league != 'All':
    filtered_df = df[df['League'] == selected_league]
else:
    filtered_df = df

# Display the filtered DataFrame
st.write(filtered_df)


