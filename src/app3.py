import altair as alt
import streamlit as st
import pandas as pd 
  
domain = ["Electricity", "Gasoline", "Natural Gas"]
range_ = ["red", "green", "blue"]
 
bar_chart = alt.Chart(energy_source).mark_bar().encode(
    x="month(Date):O",
    y="sum(Price ($)):Q",
    color=alt.Color("EnergyType", scale=alt.Scale(domain=domain, range=range_))
)
st.altair_chart(bar_chart, use_container_width=True)
