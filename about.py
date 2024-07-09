import streamlit as st

def app():

    about_text = """
    ### About Use Case Classification Bot :robot_face:

    Welcome to the **Use Case Classification Bot**, a Streamlit-powered application designed to streamline your AI project planning process. Our bot specializes in understanding and classifying your project ideas into LLM (Language Learning Model) use case archetypes, providing you with valuable insights into the necessary components for your use case.

    ### What We Do :mag:
    Our AI assistant is here to help you map your innovative ideas to specific use case archetypes. Whether you're exploring customer service automation, natural language processing tasks, or any other AI-driven project, our bot is equipped to guide you through the journey from conception to realization.

    ### Features :sparkles:
    - **Interactive Chat Interface**: Communicate your ideas through a friendly chat interface that simulates a real conversation with an AI expert.
    - **LLM Use Case Mapping**: Utilize the bot's capability to categorize your project into predefined use case archetypes.
    - **Instant Feedback**: Receive immediate guidance on the necessary building blocks for your project, including suggestions on NLP tools, chatbot platforms, and databases.
    - **Dynamic Response Simulation**: Experience human-like interactions with our simulated typing feature, enhancing the conversational feel.

    ### How It Works :gear:
    1. Share your project idea or question through the chat input.
    2. Our AI assistant analyzes your input and provides a classification along with a list of suggested components and technologies.
    3. You get a clearer picture of how to structure your AI project for success.

    ### Technology Stack :computer:
    - **Natural Language Processing (NLP)**: Leveraging state-of-the-art NLP to understand and process your requests.
    - **Streamlit**: This powerful library enables us to create this web application with ease, focusing on a great user experience.
    - **AzureGPT4Chat**: Our backend LLM that powers the intelligent responses you receive.

    ### Disclaimer :warning:
    Please note that this is a simulated conversation powered by AI. The responses generated may not always be accurate or appropriate, and should be used as a guide rather than a definitive solution.

    ### Get Started :rocket:
    Ready to take your AI project to the next level? Share your idea with our Use Case Classification Bot and let the magic happen! :sunglasses:

    For any inquiries or further assistance, please reach out to us. We are excited to be part of your AI journey! :+1:

    ---

    Made with :heart: and Streamlit
    """

    # Render the Markdown text in the app
    st.markdown(about_text, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
