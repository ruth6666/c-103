import pandas as pd 
import plotly.express as px 
df = pd.read_csv('/Users/ruth/Desktop/coding/python/c-103/data.csv')
fig = px.scatter(df,x='Population',y='Per capita',color='Country',size='Percentage')
fig.show()