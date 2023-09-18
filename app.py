import streamlit as st
import pandas as pd
import numpy as np

# Generate sample data for top shopping apps (replace with real-time data)
def generate_sample_data(num_entries):
    data = {
        'App': [f'Shopping App {i+1}' for i in range(num_entries)],
        'Rating': np.random.uniform(3.5, 5.0, num_entries).round(1),
        'Downloads (millions)': np.random.randint(100, 1000, num_entries)
    }
    return pd.DataFrame(data)

# Generate 50 sample entries
num_entries = 50
shopping_apps_data = generate_sample_data(num_entries)

st.title('Top Shopping Apps Comparison')

# Display shopping app data
st.write('Shopping App Data:')
st.write(shopping_apps_data)

# Allow user to select apps for comparison
selected_apps = st.multiselect('Select Apps for Comparison', shopping_apps_data['App'].unique())

# Filter the data based on selected apps
selected_shopping_apps = shopping_apps_data[shopping_apps_data['App'].isin(selected_apps)]

# Display the selected shopping apps
st.write('Selected Shopping Apps for Comparison:')
st.write(selected_shopping_apps)

# Add more features for comparison based on your data
