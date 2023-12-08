import streamlit as st
import pandas as pd
import json

def app():
    st.title('Archetype Database :gear:')
    st.markdown('---')
    st.write("")

    # Convert data to DataFrame
    df = pd.DataFrame(st.session_state.archetypes)

    # Display the editable DataFrame
    edited_df = st.data_editor(df, hide_index=True, height=500)
    if edited_df is not None:
      # update st.session_state.archetypes
      st.session_state.archetypes = edited_df.to_dict(orient='records')

      # Save DataFrame to JSON
      with open("archetypes.json", "w") as f:
          json.dump(edited_df.to_dict(orient='records'), f)

if __name__ == "__main__":
    app()
