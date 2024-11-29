import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# URL to raw file
url = "https://github.com/LeScott2406/TeamData/raw/refs/heads/main/Final.xlsx"

# Fetch the file from GitHub using requests
response = requests.get(url)
if response.status_code == 200:
    # Load the content of the file into pandas
    df = pd.read_excel(BytesIO(response.content))

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
else:
    st.error(f"Failed to load the file. Status code: {response.status_code}")



