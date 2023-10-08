import streamlit as st
import pandas as pd

# Set the title and header of the Streamlit app
st.title("Water Directory")
st.header("List of Water Quality in Canadian Provinces")
# Define the JSON data
data = pd.read_json("water.json")
# Create a list of dictionaries to flatten the JSON data
flat_data = []
for province, records in data["Provinces"].items():
    for record in records:
        record["Province"] = province
        flat_data.append(record)

# Create a DataFrame from the flattened data
df = pd.DataFrame(flat_data)


# Display the table in Streamlit
st.table(df)

###############
search_query = st.text_input(
    "Search for Provincial Water Quality", value="", key="search_input")

# Button to trigger the search (Ctrl + F)
ctrl_f_button = st.button("Ctrl + F")

# Convert the search query to lowercase for case-insensitive search
search_query = search_query.lower()

# Initialize a list to store matching results
matching_results = []
# Search functionality
if ctrl_f_button or search_query:
    # Iterate through rows and columns and collect matching species
    for index, row in data.iterrows():
        for col_name, cell_value in row.items():
            if search_query in str(cell_value).lower():
                matching_results.append(data.iloc[index])

    # Display a message if no results are found
    if not matching_results:
        st.warning(f"No results found for '{search_query}'")
    else:
        # Count the number of species found in the search
        st.write(f"Number of Species Found: {len(matching_results)}")
