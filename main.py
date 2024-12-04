import streamlit as st

# Initialize session state variable for navigation
if "page" not in st.session_state:
    st.session_state.page = "main"  # Default to the main page

# Page content for "main"
if st.session_state.page == "main":
    # Title of the application
  
    
    st.title("DATA STRUCTURE AND ALGORITHM MOCK EXAM 2024")

    # Display the list of names in batches
    st.subheader("List of Passers... loading.."
                )


    # Batch 1
   batch_1 = [
        "Agohob", "Albores", "Ampo", "Baguio", "Capiña", "Celeste",
        "Diaz", "Escano", "Etulle", "Itang", "Jose", "Librea", "Lim", "Lumbab",
        "Mariano", "Mendez", "Pahila", "Palamos", "Pasaol", "Perral", "Regidor",
        "Retardo", "Ricaborda", "Sampiano", "Tandingan", "Ubas", "Vasquez", "Ybañez"
    ]
    st.subheader("To God Be the Glory")
    # Display the list of names in the batch
    for name in batch_1:
        st.write(name)
