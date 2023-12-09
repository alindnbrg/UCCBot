import streamlit as st
import pandas as pd
import json
from state import set_state  # Import from state.py

def app():
    st.markdown('### Archetype Database :gear:')

    # Legend for the table columns
    st.markdown("""
    - name :point_right: *The name of the archetype*
    - keywords :point_right: *Descriptive keywords associated with the archetype*
    - implementation_notes :point_right: *your technology and servicesthat make this archetype unique*
    - business_value :point_right: *an indication of the business value provided by this archetype, along with potential metrics or indicators for quantifying it*
    """)


    st.markdown('---')
    st.write(" ")

    if len(st.session_state.archetypes) == 0:
        st.write("No archetypes found. Please import a JSON file.")
        uploaded_file = st.file_uploader("Choose a file", type="json")
        if uploaded_file is not None:
            try:
                # Update archetypes in session state using set_state
                archetypes_data = json.load(uploaded_file)
                set_state('archetypes', archetypes_data)
                st.write("Archetypes imported successfully.")
                st.rerun()
            except json.JSONDecodeError:
                st.error("Invalid JSON file.")
    else:
        df = pd.DataFrame(st.session_state.archetypes)
        # Assuming st.data_editor is a valid function (please replace with actual function)
        edited_df = st.data_editor(df, hide_index=True, height=500)
        if edited_df is not None:
            # Update archetypes in session state using set_state
            set_state('archetypes', edited_df.to_dict(orient='records'))

if __name__ == "__main__":
    app()
