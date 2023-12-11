import streamlit as st
import pandas as pd
import json
from state import set_state  # This should be a function that manages the session state.

def app():
    # Display the main title of the application.
    st.markdown('### Archetype Database :gear:')

    # Provide a legend for the table columns that will be displayed.
    st.markdown("""
    - **name**: *The name of the archetype*
    - **keywords**: *Descriptive keywords associated with the archetype*
    - **implementation_notes**: *Your technology and services that make this archetype unique*
    - **business_value**: *An indication of the business value provided by this archetype, along with potential metrics or indicators for quantifying it*
    """)

    # Ensure there's some space before the next UI element.
    st.write(" ")

    # Check if there are any archetypes in the session state and display them.
    if len(st.session_state.archetypes) > 0:
        # Convert the list of archetypes into a pandas DataFrame for display.
        df = pd.DataFrame(st.session_state.archetypes)
        # Render the DataFrame as an HTML table, omitting the index column.
        st.markdown(df.to_html(index=False), unsafe_allow_html=True)
    else:
        # Prompt the user to upload a JSON file if no archetypes are found.
        st.write("No archetypes found. Please import a JSON file.")

        # File uploader widget allows the user to upload a JSON file.
        uploaded_file = st.file_uploader("Choose a file", type="json")

        # If a file is uploaded, process the file.
        if uploaded_file is not None:
            try:
                # Load the JSON data from the uploaded file.
                archetypes_data = json.load(uploaded_file)
                # Update the session state with the new data.
                set_state('archetypes', archetypes_data)
                # Optionally save the uploaded file info in the session state.
                set_state('uploaded_file', uploaded_file)
                # Rerun the app to reflect the uploaded data.
                st.rerun()
            except json.JSONDecodeError:
                # Display an error message if the uploaded file is not a valid JSON.
                st.error("Invalid JSON file.")
        else:
            # If no file is uploaded (or it is removed), reset the archetypes in the session state.
            set_state('archetypes', [])

# Run the app function when the script is executed.
if __name__ == "__main__":
    app()
