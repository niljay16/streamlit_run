import streamlit as st

# Initialize session state variable for navigation
if "page" not in st.session_state:
    st.session_state.page = "main"  # Default to the main page

# Page content for "main"
if st.session_state.page == "main":
    # Title of the application
    st.title("DATA STRUCTURE AND ALGORITHM MOCK EXAM 2024")

    # Display the list of names in batches
    st.subheader("BATCH 1 | December 4, 2024 | 1PM TO 2PM")
    batch_1 = [
        "1. Jose, Cyrel",
        "2. Ubas, Prince Jerald",
        "3. Arnelia, Jaylord",
        "4. Palamos, Mary Chielo",
        "5. Sampiano, Nor-Ain",
        "6. Tandingan, Jirby",
        "7. Capiña, Keilah",
        "8. Watin, Sheryl Lou",
        "9. Itang, Kienneth Paul",
        "10. Pasaol, Vivian",
        "11. Agohob, Francis Luis",
        "12. Mendez, Bryle",
        "13. Abadiez, Jhony Jon",
        "14. Diaz, Adrian",
        "15. Ybañez, Micah",
        "16. Ampo, Meljan Rhyan",
        "17. Sagayno, Claire Marie",
        "18. Dalmacio, Benjie",
        "19. Regidor, Ravenala",
        "20. Lim, Jhoenell",
        "21. Ricaborda, Crystal Rhyze"
    ]

    # Display names for Batch 1
    for name in batch_1:
        st.write(name)

    # Add a divider between batches
    st.markdown("---")

    st.subheader("BATCH 2 | December 4, 2024 | 2PM TO 3PM")
    batch_2 = [
        "1. Mejias, Honey Lee",
        "2. Baguio, Edjay Mae",
        "3. Tampon, Shiehenle",
        "4. Albores, Kenneth Paul",
        "5. Capoy, Jay Bee",
        "6. Escano, Teodelyn",
        "7. Lumbab, Marianne Dominique",
        "8. Celeste, Angel Lyne",
        "9. Amorado, Yvan Kirvy Edyzon",
        "10. Perral, Brixton",
        "11. Mante, Jemar",
        "12. John Carl, Librea",
        "13. Fedriquilan, Wilfred",
        "14. Retardo, Frenz Godfrey",
        "15. Nonol, Dominique Marie",
        "16. Etulle, Rhona May",
        "17. Pahila, Jonathan Neil",
        "18. Davide, Andrian",
        "19. Mapandi, Abdulhakim",
        "20. Bandibas, Lei",
        "21. Mariano, Jerson John"
    ]

    # Display names for Batch 2
    for name in batch_2:
        st.write(name)


