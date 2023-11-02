import streamlit as st

st.markdown("Version 4. Create a merged table with most relevant exchanges, Exchange selector type, convertion rate")

#streamlit run api_data_v4.py

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
  
  # pd.concat([df1, df2], axis=1)

  df_all = df_oficial
  df_all = pd.concat([df_all, df_blue, df_bolsa])
  #df_all = pd.concat([df_all, df_bolsa], axis=1)
  st.dataframe(df_all)
  
st.markdown("Today's Most Relevant Exchange Ratios in Argentina")
All_data()


st.markdown("Select Exchange type")

selection = st.selectbox('Select exchange type', ["Dolar Oficial","Dolar Blue","Dolar Bolsa"])
st.write(selection)

def load_data(option):
    if option == "Dolar Oficial":
       url = 'https://dolarapi.com/v1/dolares/oficial'
    elif option == "Dolar Blue":
       url = 'https://dolarapi.com/v1/dolares/blue'
    else:
       url = 'https://dolarapi.com/v1/dolares/bolsa'
    
    r = requests.get(url)
    json = r.json()
    df = pd.DataFrame(json, index=[0])
    st.dataframe(df)
    return df



cot = load_data(selection)



monto_buy = st.number_input('Type amount to convert to compra (buy)') 
total_buy = pd.to_numeric(cot.iloc[0]['compra']) * monto_buy
st.write(total_buy)

monto_mix = st.number_input('Type amount to convert to compra (MIX)') 
total_mix = pd.to_numeric(cot.iloc[0]['compra']) + pd.to_numeric(cot.iloc[0]['venta'])
total_mix = total_mix / 2
total_mix = total_mix * monto_mix
st.write(total_mix)

monto_sell = st.number_input('Type amount to convert to Venta (sell)')
total_sell = pd.to_numeric(cot.iloc[0]['venta']) * monto_sell
st.write(total_sell)


st.write("Developed by Pedro Ciancaglini - https://www.linkedin.com/in/pedrociancaglini/")
