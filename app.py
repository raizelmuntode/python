import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for top shopping apps (replace with real-time data)
def generate_sample_data(num_entries):
    data = {
        'App': [f'{i+1}' for i in range(num_entries)],
        'Rating': np.random.uniform(3.5, 5.0, num_entries).round(1),
        'Downloads (millions)': np.random.randint(100, 1000, num_entries)
    }
    return pd.DataFrame(data)

# Function to simulate user login (replace with actual authentication logic)
def authenticate(username, password):
    return username == 'user' and password == 'password'

# Generate 50 sample entries
num_entries = 50
shopping_apps_data = generate_sample_data(num_entries)

# Main Streamlit app
def main():
    st.title('Login Page')

    # Get user input for username and password
    username = st.text_input('Username:')
    password = st.text_input('Password:', type='password')

    # Check if the login button is pressed
    if st.button('Login'):
        if authenticate(username, password):
            st.success('Login successful!')
            display_comparison(shopping_apps_data)
        else:
            st.error('Invalid credentials. Please try again.')

# Function to display the comparison
def display_comparison(data):
    st.title('Top Shopping Apps Comparison')

    # Allow user to select apps for comparison
    selected_apps = st.multiselect('Select Apps for Comparison', data['App'].unique(), default=data['App'].tolist())

    # Filter the data based on selected apps
    selected_shopping_apps = data[data['App'].isin(selected_apps)]

    # Display the selected shopping apps
    st.write('Selected Shopping Apps for Comparison:')
    st.write(selected_shopping_apps)

    # Plot a bar chart for rating comparison
    st.write('### Ratings Comparison')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Adjust the bar width to add space between the bars
    bar_width = 0.4
    bar_positions = np.arange(len(selected_shopping_apps))
    ax.bar(bar_positions, selected_shopping_apps['Rating'], width=bar_width, tick_label=selected_shopping_apps['App'])
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    st.pyplot(fig)

    # Plot a figure for download counts
    st.write('### Download Counts')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(selected_shopping_apps['App'], selected_shopping_apps['Downloads (millions)'], marker='o')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

# Run the app
if __name__ == '__main__':
    main()
