import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Custom CSS styles
custom_css = """
<style>
body {
    background-image: linear-gradient(to bottom, #ffcccb, #ff6666); /* Set a gradient background */
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
    font-family: Arial, sans-serif;
    color: white; /* Change text color to white */
}
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Set the title and header of the Streamlit app
st.title("Marine Animals Directory")
st.header("List of Marine Animals")

# Your Streamlit app content here
# st.write("This is your Streamlit app content.")
# Load the data from the local JSON file
data = pd.read_json("species.json")

# Create a search bar and filter the data
search_query = st.text_input(
    "Search for Any Species", value="", key="search_input")

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

# Display matching results in a table with a danger emoji for endangered species
if matching_results:
    st.subheader(f"Results for '{search_query}':")
    result_df = pd.concat(matching_results, axis=1).T

    # Check if the "SARA status" column exists before applying emoji
    if "SARA status" in result_df.columns:
        # Replace "Endangered" with the danger emoji 🚨 in the "SARA status" column
        result_df['SARA status'] = result_df['SARA status'].apply(
            lambda x: '🚨' if x == 'Endangered' else x)

    # Check if the "URL" column exists before applying the link
    if "URL" in result_df.columns:
        result_df['URL'] = result_df.apply(
            lambda row: f"[Link]({row['URL']})", axis=1)

    st.write(result_df, unsafe_allow_html=True)

# Display the full table by default
st.subheader("Full Table:")
st.write(data)

# Add a download button to download the filtered data as a CSV file
if matching_results:
    st.subheader("Download Filtered Data")
    csv_data = result_df.to_csv(index=False, encoding='utf-8-sig')
    st.download_button("Download CSV", csv_data, "filtered_data.csv", key="download_button")



# Create a link to App 2
app2_link = "[Go to App 2](http://localhost:8502)"
st.markdown(app2_link, unsafe_allow_html=True)


# Check if matching results exist and the "SARA status" column is present
if matching_results and "SARA status" in result_df.columns:
    st.subheader("Pie Chart of SARA Status")

    # Count the occurrences of each SARA status
    sara_status_counts = result_df['SARA status'].value_counts()

    # Create labels and sizes for the pie chart
    labels = sara_status_counts.index
    sizes = sara_status_counts.values

    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular

    # Display the pie chart in Streamlit
    st.pyplot(fig)
