import streamlit as st
import altair as alt
import os
import pandas as pd

# Get the absolute path to the image file
image_path = os.path.abspath('1-1.png')

# Create a list with the absolute path
image_urls = [image_path]

for url in image_urls:
    st.image(url, use_column_width=False)

dataframe = pd.read_json('waterQ.json')
st.write(dataframe.size)

option = st.selectbox(
    'Statistics for Water Quality:',
    [str(year) for year in range(2000, 2023)])

find_button = st.button("Look at Statistics")

if find_button:
    dataframe_new = dataframe[dataframe['DATE'].dt.year == int(option)]
    st.write(dataframe_new)
    # extract the two columns in the graph
    selected_columns = dataframe_new[['VARIABLE', 'VALUE_VALEUR']]
    st.write(selected_columns)

    chart = alt.Chart(selected_columns).mark_line(color='blue').encode(  # Line graph
        x='VARIABLE',
        y='VALUE_VALEUR',
        tooltip=['VARIABLE', 'VALUE_VALEUR']
    ).properties(
        title='Line Graph of Water Concentration',
        width=700,
        height=400
    )
    st.altair_chart(chart, use_container_width=True)
