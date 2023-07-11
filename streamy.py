import streamlit as st

def main():
    st.title("File Upload Example")
    
    # Display a file uploader widget
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        # Process the uploaded file
        content = uploaded_file.read()
        st.text("File content:")
        st.write(content)
        
if __name__ == "__main__":
    main()