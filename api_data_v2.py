import streamlit as st

st.markdown("Version 2. Bringing data from API")

import pandas as pd
import requests

# This was part of version 1
# url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
# r = requests.get(url)
# json = r.json()
# df = pd.DataFrame(json, index=[0])

new_url = st.text_input('Enter URL API with Anonymous Access')

load_data(new_url)
#st.button("Show API Data", on_click=load_data(new_url))

#@st.cache
def load_data(url='https://api-dolar-argentina.herokuapp.com/api/dolaroficial'):
    # url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
    r = requests.get(url)
    json = r.json()
    df = pd.DataFrame(json, index=[0])
    st.dataframe(df)
    #return df

#def ShowData():
#    st.dataframe(load_data(url))


