import streamlit as st
import matplotlib.pyplot as plt
import altair as alt


st.image('1-1.png', use_column_width=False)

import datetime as dt
import pandas as pd
dataframe = pd.read_json('Water-Qual-Eau-Churchill-2000-present.json')

#displays the current size of the data
#st.write(dataframe.size)

#combo box with all year options
option = st.selectbox(
    'Statistics for Water Quality:',
    ('2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'))

#button for will find statistics for that year
find_button = st.button("Look at Statistics")

#if the button is clicked
if find_button:
    #creates a new dataframe the values onn in that year
    dataframe_new = dataframe[dataframe['DATE'].dt.year == int(option)]
    #displays that dataframe on the screen
    st.write(dataframe_new)
    #extract the two columns in the graph
    selected_columns = dataframe_new[['VARIABLE', 'VALUE_VALEUR']]

    #displays the concentration and name of chemical dataframe
    st.write(selected_columns)

    #assign the values for x and y pairs for the bar graph
    x_values = selected_columns['VARIABLE']
    y_values = selected_columns['VALUE_VALEUR']


    # plt.figure(figsize=(100,600))

    #plot the values making the values for x value the variable and y value for the concentration value
    plt.bar(x_values, y_values)
    #this is for vertical values
    #plt.barh(y_values, x_values)

    #write credentials for graph
    plt.xlabel('Chemical Name')
    plt.ylabel('Concentration')
    #horizontal bars
    #crammed bar graph


    #loop -- find the ones you are looking for in the look 


    #filter want to average 

    plt.title('Bar Graph of Water Concentration')
    plt.savefig('bar_plot.png')
    st.image('bar_plot.png', use_column_width=True)
