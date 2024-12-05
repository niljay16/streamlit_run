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

    # Batch 1 (list of tuples with name and new score)
    batch_1 = [
        ("Regidor", 92.8),
        ("Pahila", 91.6),
        ("Ubas", 91.6),
        ("Perral", 90.4),
        ("Retardo", 90.4),
        ("Sampiano", 90.4),
        ("Ybañez", 90.4),
        ("Albores", 89.2),
        ("Ampo", 89.2),
        ("Librea", 89.2),
        ("Lumbab", 89.2),
        ("Escano", 88),
        ("Lim", 88),
        ("Itang", 86.8),
        ("Celeste", 84.4),
        ("Diaz", 84.4),
        ("Agohob", 83.2),
        ("Capiña", 83.2),
        ("Mendez", 83.2),
        ("Tandingan", 83.2),
        ("Baguio", 82),
        ("Etulle", 82),
        ("Mariano", 82),
        ("Ricaborda", 80.8),
        ("Palamos", 79.6),
        ("Vasquez", 79.6),
        ("Jose", 76),
        ("Pasaol", 76),
        ("Jay Bee Capoy", 73.6),
        ("Abadiez", 88.2),
        ("Amorado", 88.1),
        ("Bandibas", 80.2),
        ("Dalmacio", 82.6),
        ("Davide", 88.4),
        ("Fedriquilan", 78.9),
        ("Mante", 80.2),
        ("Mapandi", 84.0),
        ("Mejias", 82.2),
        ("Sagayno", 82.1),
        ("Tampon", 84.6),
        ("Watin", 82.4)
    ]

    st.subheader("To God Be the Glory")
    # Display the list of names with numbering and their corresponding scores
    for idx, (name, score) in enumerate(batch_1, start=1):
        st.write(f"{idx}. {name} - {score}")
