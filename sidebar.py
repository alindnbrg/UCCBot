import streamlit as st
import home
import about
import archetypes
from state import clear_state, set_state

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
        Statistics
        * analyzed use cases: {use_case_count()}
        * archetypes: {len(st.session_state.archetypes)}
        """
    )
    st.sidebar.write(" ")


    # add a password type textfiled to the sidebar
    api_token = st.sidebar.text_input(
        "ai platform token", type="password", value=st.session_state.api_token)
    if api_token:
        set_state("api_token", api_token)

    st.sidebar.write(" ")

    if st.sidebar.button('Reset application'):
        clear_state()
        st.rerun()

    st.sidebar.write(" ")

    st.sidebar.markdown(
        '<a href="mailto:andre.lindenberg@exxeta.com?subject=Use Case Classification Bot" target="_blank">Feedback?</a> &nbsp; :mailbox_with_no_mail:',
        unsafe_allow_html=True
    )

    return PAGES[page]

if __name__ == "__main__":
    app()
