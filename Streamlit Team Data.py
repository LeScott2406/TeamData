import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# URL to raw file
url = "https://github.com/LeScott2406/TeamData/raw/refs/heads/main/Final.xlsx"

# Attempt to fetch the file from GitHub using requests
st.write("Fetching file from GitHub...")
try:
    response = requests.get(url)
    response.raise_for_status()  # Will raise an HTTPError for bad responses (4xx, 5xx)
    st.write("File fetched successfully!")

    # Load the content of the file into pandas
    df = pd.read_excel(BytesIO(response.content))
    st.write("File loaded into DataFrame")

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

except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch the file: {e}")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
