import pandas as pd

df = pd.read_html('https://en.wikipedia.org/wiki/Poverty')
df[1]
