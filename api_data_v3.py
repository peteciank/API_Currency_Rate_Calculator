import streamlit as st

st.markdown("Version 3. Bringing data from API, using a selector to choose Exchange types, and converting ratios for 'compra' and 'venta'")

import pandas as pd
import requests

# new_url = st.text_input('Enter URL API with Anonymous Access')
# url='https://api-dolar-argentina.herokuapp.com/api/dolaroficial'

selection = st.selectbox('Seleccionar Tipo de Cambio', ["Dolar Oficial","Dolar Blue","Dolar Bolsa"])
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



monto = st.number_input('Ingresar Monto a convertir para la compra')
total = pd.to_numeric(cot.iloc[0]['compra']) * monto
st.write(total)


monto = st.number_input('Ingresar Monto a convertir para la Venta')
total = pd.to_numeric(cot.iloc[0]['venta']) * monto 
st.write(total)


