import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np

st.title('World Wide Poverty Table')

st.markdown("""
This app retrieves the list of the Regions (from Wikipedia) and its corresponding Poverty rates until 2018!
* **Python libraries:** base64, pandas, streamlit, yfinance, numpy, matplotlib
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/Poverty).
""")


#st.markdown("""
#This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding **stock closing price** (year-to-date)!
#* **Python libraries:** base64, pandas, streamlit, yfinance, numpy, matplotlib
#* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
#                                >>> UPDATE NOW> https://en.wikipedia.org/wiki/Poverty
# """)

st.sidebar.header('User Input Features')

# Web scraping of S&P 500 data
#
@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/Poverty'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df

df = load_data()
sector = df.groupby('Region')

# Sidebar - Sector selection
sorted_sector_unique = sorted( df['Region'].unique() )
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtering data
df_selected_sector = df[ (df['Region'].isin(selected_sector)) ]

st.header('Display Selected Regions')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

# Download Poverty Data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="Poverty.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)



num_company = st.sidebar.slider('Number of Regions', 1, 5)
