import streamlit as st

# Initialize session state variable for navigation
if "page" not in st.session_state:
    st.session_state.page = "main"  # Default to the main page

# Page content for "main"
if st.session_state.page == "main":
    # Title of the application
    st.subheader("Polytechnic College of Davao Del Sur")
    st.subheader("Student Council of Information Technology")
    
    st.title("DATA STRUCTURE AND ALGORITHM MOCK EXAM 2024")

    # Display the list of names in batches
    st.subheader("List of Passers...")

    # Batch 1
    batch_1 = [
     
    ]

    # Display the list of names in the batch
    for name in batch_1:
        st.write(name)
