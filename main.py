import streamlit as st

# Initialize session state variable for navigation
if "page" not in st.session_state:
    st.session_state.page = "main"  # Default to the main page

# Page content for "main"
if st.session_state.page == "main":
    # Title of the application
    st.title("DATA STRUCTURE AND ALGORITHM MOCK EXAM 2024")

    # Display the list of names in batches
    st.subheader("List of Passers.")

    # Batch 1 (list of tuples with name and score)
    batch_1 = [
        ("Regidor ", 44),
        ("Pahila", 43),
        ("Ubas", 43),
        ("Perral", 42),
        ("Retardo", 42),
        ("Sampiano", 42),
        ("Ybañez", 42),
        ("Albores", 41),
        ("Ampo", 41),
        ("Librea", 41),
        ("Lumbab", 41),
        ("Escano", 40),
        ("Lim", 40),
        ("Itang", 39),
        ("Celeste", 37),
        ("Diaz", 37),
        ("Agohob", 36),
        ("Capiña", 36),
        ("Mendez", 36),
        ("Tandingan", 36),
        ("Baguio", 35),
        ("Etulle", 35),
        ("Mariano", 35),
        ("Ricaborda", 34),
        ("Palamos", 33),
        ("Vasquez", 33),
        ("Jose", 30),
        ("Pasaol", 30),
        ("Jay Bee Capoy", 28)
    ]

    st.subheader("To God Be the Glory")
    # Display the list of names with numbering and their corresponding scores
    for idx, (name, score) in enumerate(batch_1, start=1):
        st.write(f"{idx}. {name} - {score}")
