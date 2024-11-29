import streamlit as st
import pandas as pd

# Use the GitHub URL where the Excel file is stored
url = "https://github.com/LeScott2406/TeamData/raw/refs/heads/main/Final.xlsx"

# Load the Excel file from GitHub
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
