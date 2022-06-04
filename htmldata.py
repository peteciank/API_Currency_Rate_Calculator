import pandas as pd
import streamlit as st


df = pd.read_html('https://en.wikipedia.org/wiki/Poverty')
df[1]
