import statistics
import plotly.graph_objects as go
import plotly.Figure_fatcory as pf
import pandas as pd 
import random
import csv

df = pd.read_csv("data.csv")

student_df = df.loc[df['student_id']=="TRL_xsl"]

print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x=student_df.groupby("level")["attempt"].mean(),
    y=('Level 1','Level 2','Level 3','Level 4'),
    orientation='h'))

fig.show()