import streamlit as st

st.markdown("Version 4. Create a merged table with most relevant exchanges, Exchange selector type, convertion rate.")

import pandas as pd
import requests

# new_url = st.text_input('Enter URL API with Anonymous Access')
# url='https://api-dolar-argentina.herokuapp.com/api/dolaroficial'

def All_data():
  #r = requests.get(url)
  #url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
  url_oficial = 'https://dolarapi.com/v1/dolares/oficial'
  url_blue = 'https://dolarapi.com/v1/dolares/blue'
  url_bolsa = 'https://dolarapi.com/v1/dolares/bolsa'
  
  df_oficial = pd.DataFrame(requests.get(url_oficial).json(), index=[0])
  df_blue = pd.DataFrame(requests.get(url_blue).json(), index=[0])
  df_bolsa = pd.DataFrame(requests.get(url_bolsa).json(), index=[0])
  
  df_all = df_oficial
  df_all = df_all.append(df_blue, ignore_index=True)
  df_all = df_all.append(df_bolsa, ignore_index=True)
  st.dataframe(df_all)
  
st.markdown("Today's Most Relevant Exchange Ratios in Argentina")
All_data()


st.markdown("Select Exchange type")

selection = st.selectbox('Select exchange type', ["Dolar Oficial","Dolar Blue","Dolar Bolsa"])
st.write(selection)

def load_data(option):
    if option == "Dolar Oficial":
       url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
    elif option == "Dolar Blue":
       url = 'https://api-dolar-argentina.herokuapp.com/api/dolarblue'
    else:
       url = 'https://api-dolar-argentina.herokuapp.com/api/dolarbolsa'
    
    r = requests.get(url)
    json = r.json()
    df = pd.DataFrame(json, index=[0])
    st.dataframe(df)
    return df



cot = load_data(selection)



monto = st.number_input('Type amount to convert to compra (buy)') 
total = pd.to_numeric(cot.iloc[0]['compra']) * monto
st.write(total)


monto = st.number_input('Type amount to convert to Venta (sell)')
total = pd.to_numeric(cot.iloc[0]['venta']) * monto 
st.write(total)

