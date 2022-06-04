import pandas as pd
import streamlit as st
import base64
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

df = pd.read_html('https://en.wikipedia.org/wiki/Poverty')
df[1]
