# state.py

import streamlit as st
import pickle
import os

# Path to the file where the session state will be stored
SESSION_STATE_PATH = "./session_state.pkl"

def init_state():
    """
    Initializes the session state with default values.
    """
    if os.path.exists(SESSION_STATE_PATH):
        load_state()
    else:
        # initialize the session state with default values
        st.session_state['messages'] = []
        st.session_state['archetypes'] = []
        st.session_state['api_token'] = None
        st.session_state['api_model'] = None

        st.session_state['prompt_template'] = f"""
            you know about the following list of llm use case archetypes:
            {st.session_state.archetypes}

            For the GenAI LLM Use provided below, please do the following:
            1. Categorize the use case based on the provided archetypes. If
            a use case cannot be categorized, create a new archetype. Only do that,
            if absolutely necessary.
            2. Briefly describe its technical implementation
            by naming required components, examplary products and technologies,
            and how the are used to implement the use case
            3. Describe the business value of the use case and try to quantify it;
            use charts, tables where appropriate.

            Break your answer down into several paragraphs.
            Use syntax highlighting for code snippets,
            and links to external resources.
            Use colored text or emojis to highlight important parts.

            If the prompt does not look like an LLM use case to you,
            respond politly that you are only interested in LLM use cases.

            Make the output look great on a streamlit page.

            LLM Use Case:\n\n
          """

        # add a first initial message to the session state
        st.session_state['messages'] = [
            {"role": "assistant",
              "content": """
              Hello! I'm your AI assistant specialized in classifying use cases.
              Tell me about your project or idea, and I'll help you map it to
              the right GenAI category and implementation archetype.
              I can also guide you through the necessary components to bring
              your vision to life. Let's get started!
              """}
        ]

        st.session_state.disclaimer = """
            Please note that you are interacting with an automated AI assistant. This assistant uses advanced language models to generate responses based on the input it receives. Here are a few important points to consider:

            - **AI Limitations:** The AI does not have personal experiences or emotions. Its responses are generated based on patterns in data and may not always accurately understand or reflect human emotions or nuances.
            - **Privacy:** Do not share sensitive, personal, or confidential information. The AI does not have the ability to retain or recall personal data unless it is part of the current session's context.
            - **Accuracy and Appropriateness:** While we strive for accuracy, the AI's responses are not infallible and should not be taken as expert advice. Responses may sometimes be inappropriate or incorrect.
            - **Feedback:** Your interactions help improve the AI. If you encounter issues, please provide feedback to help us enhance the AI's performance.
        """

        st.session_state.no_archetypes_message = """
            No archetypes found. Please upload archetypes to proceed.
        """

def load_state():
    """
    Loads the session state from a file, if it exists.
    """
    with open(SESSION_STATE_PATH, "rb") as f:
        loaded_state = pickle.load(f)
        for key, value in loaded_state.items():
            st.session_state[key] = value

def save_state():
    """
    Saves the current session state to a file.
    """
    with open(SESSION_STATE_PATH, "wb") as f:
        pickle.dump(dict(st.session_state), f)

def set_state(key, value):
    """
    Sets a value in the session state and saves the entire state to a file.

    Args:
    key (str): The key in the session state to set.
    value: The value to set for the given key.
    """
    st.session_state[key] = value
    save_state()

def clear_state():
    """
    Clears the session state and deletes the session state file.
    """
    # get the first message from the session state
    st.session_state.clear()
    if os.path.exists(SESSION_STATE_PATH):
        os.remove(SESSION_STATE_PATH)

    # initialize the session state with default values
    init_state()

