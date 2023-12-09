import streamlit as st
import home
import about
import archetypes
from state import clear_state

PAGES = {
    "Home": home,
    "Archetypes": archetypes,
    "About": about,
}

def use_case_count():
    return int((len(st.session_state.messages)-1)/2) if len(st.session_state.messages) > 0 else 0

def app():
    st.sidebar.image("resources/logo_light.svg", width=125)
    st.sidebar.write("hightech with a heartbeat")

    page = st.sidebar.radio("Choose a page:", list(PAGES.keys()))

    st.sidebar.write(" ")
    st.sidebar.markdown(
        f"""

        Configuration:
        * analyzed use cases: {use_case_count()}
        * your archetypes: {len(st.session_state.archetypes)}
        """
    )
    st.sidebar.write(" ")

    if st.sidebar.button('Reset application'):
        clear_state()
        st.rerun()

    return PAGES[page]

if __name__ == "__main__":
    app()
