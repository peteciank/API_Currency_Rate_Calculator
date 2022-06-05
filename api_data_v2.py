import streamlit as st

st.markdown("Version 2. Bringing data from API")

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


#def ShowData():
#    st.dataframe(load_data(url))

load_data(selection)
