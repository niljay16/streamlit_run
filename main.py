import streamlit as st

# Initialize session state variable for navigation
if "page" not in st.session_state:
    st.session_state.page = "main"  # Default to the main page

# Page content for "main"
if st.session_state.page == "main":
    # Title of the application
    st.title("DATA STRUCTURE AND ALGORITHM MOCK EXAM 2024")

    # Display the list of names in batches
    st.subheader("List of Passer")
    batch_1 = [
      
    
    ]
