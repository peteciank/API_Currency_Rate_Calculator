import streamlit as st

st.markdown("Hello George. This is Peter.")

import pandas as pd
import requests

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
