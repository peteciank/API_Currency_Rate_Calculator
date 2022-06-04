import streamlit as st

st.markdown("Hello World. This is Peter.")

import pandas as pd
import requests

url = 'https://api-dolar-argentina.herokuapp.com/api/evolucion/dolaroficial'
r = requests.get(url)
json = r.json()
df = pd.DataFrame(json['meses'])


st.markdown(df)
