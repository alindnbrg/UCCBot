# sidebar.py

import streamlit as st
import json
import home
import about
import archetypes

# Define the pages
PAGES = {
    "Home": home,
    "Archetypes": archetypes,
    "About": about,
}

def load_archetypes():
    with open("archetypes.json", "r") as f:
        archetypes_data = json.load(f)
    if "archetypes" not in st.session_state:
        st.session_state.archetypes = archetypes_data

def clear_messages():
    if 'messages' in st.session_state and len(st.session_state.messages) > 1:
        # Keep the first message and clear the rest
        st.session_state.messages = st.session_state.messages[:1]
        # Rerun the app to update the UI
        st.experimental_rerun()

def app():
    st.sidebar.image("img/logo_light.svg", width=125)  # Replace with your logo path
    st.sidebar.write("hightech with a heartbeat")

    page = st.sidebar.radio("Choose a page:", list(PAGES.keys()))
    load_archetypes()  # Load or initialize the archetypes in session state

    # Clear button
    if st.sidebar.button('Clear use cases'):
        clear_messages()
    return PAGES[page]
