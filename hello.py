import streamlit as st

st.markdown("Version 1. Bringing data from API")

import pandas as pd
import requests

# Source of APIs https://github.com/Castrogiovanni20/api-dolar-argentina

# Code for historical evolution of Dollar in Argentina
#url = 'https://api-dolar-argentina.herokuapp.com/api/evolucion/dolaroficial'
#r = requests.get(url)
#json = r.json()
#df = pd.DataFrame(json['meses'])

url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
r = requests.get(url)
json = r.json()
df = pd.DataFrame(json, index=[0])

st.dataframe(df)

#st.markdown(df)
