"""
I decided to plot the webapp graph showing the temperature performance
being scraped by the oython program
"""

# import libraries
import streamlit as st
import plotly.express as px
import pandas as pd


# The data_2.txt file shows our data is been seperated by commas, which makes it a csv
# Using pandas to import the csv
data = pd.read_csv("data_2.txt")

fig = px.line(
                x=data["date"], y=data["temperature"],
                labels = {"x": "Date", "y": "Temperature (C) "}
              )

# Plot visual
st.plotly_chart(fig)
