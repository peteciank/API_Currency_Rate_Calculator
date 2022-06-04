import streamlit as st

st.markdown("Version 1. Bringing data from API")

import pandas as pd
import requests

url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
r = requests.get(url)
json = r.json()
df = pd.DataFrame(json, index=[0])

st.dataframe(df)

#st.markdown(df)
