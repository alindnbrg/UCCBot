import streamlit as st
import ai
import time
from state import set_state  # Import from state.py

# Initialize the LLM object
llm = ai.AzureGPT4Chat()

# Render chat messages
def render_messages(messages):
    # Display chat messages from history
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def app():
    st.subheader("Use Case Classifier")

    # Check if archetypes are available
    if len(st.session_state.archetypes) == 0:
        st.info(st.session_state.no_archetypes_message)
        return  # Return early to prevent showing the chat interface

    with st.expander("Disclaimer"):
        st.write(st.session_state.disclaimer)

    render_messages(st.session_state.messages)

    # Accept user input
    if prompt := st.chat_input("Share your idea or ask a question..."):

        # display the messages in the chat
        render_messages([{"role": "user", "content": prompt}])

        # Update chat history with user message
        updated_messages = st.session_state.messages + [{"role": "user", "content": prompt}]
        set_state('messages', updated_messages)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            with st.spinner("thinking... 🤔"):
                assistant_response = llm(prompt)
                time.sleep(1)

            for chunk in assistant_response.split(' '):
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

        # Update chat history with assistant's response
        updated_messages = st.session_state.messages + [{"role": "assistant", "content": full_response}]
        set_state('messages', updated_messages)
        st.rerun()

if __name__ == "__main__":
    app()
