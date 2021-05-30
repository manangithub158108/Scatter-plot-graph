import pandas as pd;
import plotly_express as px;

dataFrame = pd.read_csv('CovidData.csv');
fig = px.scatter(dataFrame, x = 'date', y = 'cases', color = 'country');
fig.show();