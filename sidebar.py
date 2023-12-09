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

    page = st.sidebar.radio("Choose a page", list(PAGES.keys()))

    st.sidebar.write(" ")
    st.sidebar.markdown(
        f"""
        Configuration
        * analyzed use cases: {use_case_count()}
        * archetypes: {len(st.session_state.archetypes)}
        """
    )
    st.sidebar.write(" ")

    if st.sidebar.button('Reset application'):
        clear_state()
        st.rerun()

    st.sidebar.write(" ")
    st.sidebar.markdown(
        '<a href="mailto:andre.lindenberg@exxeta.com?subject=Use Case Classification Bot" target="_blank">Have a question?</a> :mailbox_with_no_mail:',
        unsafe_allow_html=True
    )

    return PAGES[page]

if __name__ == "__main__":
    app()
