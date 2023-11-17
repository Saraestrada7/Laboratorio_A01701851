import streamlit as st
import pandas as pd
import numpy as np
import plotly as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from bokeh.plotting import figure

st.title('Police incident reports from 2018 to 2020 in San Francisco')

df = pd.read_csv('Police.csv')

st.markdown('The data shown below belongs to incident reports in the City of San Francisco, from the year 2018 to 2020, woth details from each case such as date, day of the week, police district, neighbourhood in which it happened, type of incident in category and subcategory, exact location and resolution')

mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['District'] = df['Police District']
mapa['Neighbourhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()
