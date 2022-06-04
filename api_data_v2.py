import streamlit as st

st.markdown("Version 2. Bringing data from API")

import pandas as pd
import requests

# This was part of version 1
# url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
# r = requests.get(url)
# json = r.json()
# df = pd.DataFrame(json, index=[0])

url = st.text_input('Enter URL API with Anonymous Access')

@st.cache
def load_data(url):
    # url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
    r = requests.get(url)
    json = r.json()
    df = pd.DataFrame(json, index=[0])
    return df



st.dataframe(df)
