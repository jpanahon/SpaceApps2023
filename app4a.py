import streamlit as st
import altair as alt
import os
import pandas as pd

st.image('src/1-1.png', use_column_width=False)

dataframe = pd.read_json('waterquality.json')

option = st.selectbox(
    'Statistics for Water Quality:',
    [str(year) for year in range(2000, 2023)])

find_button = st.button("Look at Statistics")

st.write("All chemicals tested:")
st.write(dataframe["VARIABLE"].unique())


if find_button:
    dataframe_new = dataframe[dataframe['DATE'].dt.year == int(option)]
    st.write(dataframe_new)
    # extract the two columns in the graph
    selected_columns = dataframe_new[['VARIABLE', 'VALUE_VALEUR']]
    st.write(selected_columns)

    chart = alt.Chart(selected_columns).mark_line(color='blue').encode(
        x=alt.X('VARIABLE', title='Chemical Name'), 
        y=alt.Y('VALUE_VALEUR', title='Concentration'),
        tooltip=['VARIABLE', 'VALUE_VALEUR']
    ).properties(
        title='Line Graph of Water Concentration',
        width=700,
        height=400
    )
    st.altair_chart(chart, use_container_width=True)
