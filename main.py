
import streamlit as st

import pandas as pd
import numpy as np
import os
import subprocess

def main():
    st.title("File Upload and Git Push Example")
    
    # Display a file uploader widget
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        file_path = os.path.join("/tmp", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        
        # Add, commit, and push the file to Git
        git_add = subprocess.run(["git", "add", file_path])
        git_commit = subprocess.run(["git", "commit", "-m", "Added file"])
        git_push = subprocess.run(["git", "push", "origin", "master"])
        
        if git_push.returncode == 0:
            st.success("File uploaded and pushed to Git successfully!")
        else:
            st.error("Failed to push the file to Git.")
    
if __name__ == "__main__":
    main()


 

st.title('uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

  


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data



data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

hour_to_filter = st.slider('hour', 0, 23, 17)

filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)


def file_upload_example():
    st.title("File Upload Example")
    
    # Display a file uploader widget
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        # Process the uploaded file
        content = uploaded_file.read()
        st.text("File content:")
        st.write(content)

def contact_us():
    st.title("Contact Us")
    
    # Add your contact information
    st.write("For any inquiries, please reach out to us at:")
    st.write("- Email: contact@example.com")
    st.write("- Phone: +1 123-456-7890")
    
    # Add a button to redirect to the HTML page
    if st.button("Visit our Website"):
        # Replace "path/to/your/html/file.html" with the actual path to your HTML file
         st.markdown(r'<a href="/pages/hel.html" target="_blank">Click here</a>', unsafe_allow_html=True)

def main():
    file_upload_example()
    contact_us()

if __name__ == "__main__":
    main()
