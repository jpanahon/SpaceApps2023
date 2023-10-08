import streamlit as st
import pandas as pd

# Custom CSS styles
custom_css = """
<style>
body {
    background-color: red; /* Set the background color to red */
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}
</style>
"""
st.image("1-1.png", use_column_width=False)
# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Set the title and header of the Streamlit app
st.title("Marine Animals Directory")
st.header("List of Marine Animals")

# Load the data from the local JSON file
data = pd.read_json("mine.json")


# Create a search bar and filter the data
search_query = st.text_input("", placeholder="Search for Any Species 🔍", key="search_input")


# Button to trigger the search (Ctrl + F)
ctrl_f_button = st.button("Search For Item")

# Convert the search query to lowercase for case-insensitive search
search_query = search_query.lower()

# Initialize a list to store matching results
matching_results = []

# Search functionality
# if ctrl_f_button or search_query:
#     # Iterate through rows and columns and collect matching species
#     for index, row in data.iterrows():
#         for col_name, cell_value in row.items():
#             if search_query in str(cell_value).lower():
#                 matching_results.append(data.iloc[index])

if ctrl_f_button or search_query:
    # Iterate through rows and columns and collect matching species
    for index, row in data.iterrows():
        if search_query in str(row).lower():
            matching_results.append(data.iloc[index])

    # Display a message if no results are found
    if not matching_results:
        st.warning(f"No results found for '{search_query}'")

# Display matching results in a single table
if matching_results:
    st.subheader(f"Results for '{search_query}':")
    result_df = pd.concat(matching_results, axis=1).T
    st.write(result_df)


# Display the full table by default
st.subheader("Full Table:")
st.dataframe(data)



