import pandas as pd
import plotly.express as px
df=pd.read_csv("https://raw.githubusercontent.com/nsinturi07/csv/main/Copy%2Bof%2Bdata%2B-%2Bdata.csv")
chart=px.line(df,x="Year", y="Per capita income", color="Country", title="per capita incomes of countries")
chart.show()

