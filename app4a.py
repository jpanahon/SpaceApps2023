import streamlit as st
import altair as alt
import os
import pandas as pd

#title for page
st.title("Churchill, Manitoba Water Quality Directory")

#open the image
st.image('1-1.png', use_column_width=False)

#open as a data frame
dataframe = pd.read_json('waterquality.json')

#open with a combobox with all the years
option = st.selectbox(
    'Search by Year Statistics for Water Quality:',
    [str(year) for year in range(2000, 2023)])

#button to activate search
find_button = st.button("Look at Statistics")

#table that displays all the chemicals tested
st.write("All chemicals tested:")
st.write(dataframe["VARIABLE"].unique())


#if button is clicked
if find_button:
    #creates a new dataframe with the filtered by years
    dataframe_new = dataframe[dataframe['DATE'].dt.year == int(option)]
    st.write(dataframe_new)
    # extract the two columns in the graph
    selected_columns = dataframe_new[['VARIABLE', 'VALUE_VALEUR']]
    st.write(selected_columns)

    #create a chart with the graph content
    chart = alt.Chart(selected_columns).mark_line(color='blue').encode(  # Line graph
        x=alt.X('VARIABLE', title="Chemical"),
        y=alt.Y('VALUE_VALEUR', title="Concentration"),
        tooltip=['VARIABLE', 'VALUE_VALEUR']
    ).properties(
        title='Line Graph of Water Concentration',
        width=700,
        height=400
    )
    #display chart on screen
    st.altair_chart(chart, use_container_width=True)
