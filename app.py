# app.py

import streamlit as st
import sidebar
from state import init_state

def main():
    init_state()
    # Load the selected page from sidebar
    page = sidebar.app()
    # Load the selected page app
    page.app()

if __name__ == "__main__":
    main()
