import streamlit as st
import os
from typing import Any
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import AzureChatOpenAI
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema.messages import HumanMessage

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-07-01-preview"
os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_EXXETA_API_TOKEN")
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")

class AzureGPT4Chat():
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.model = "gpt-4"
    self.deployment_name = "exxetagpt-pro"
    self.llm = AzureChatOpenAI(
      model=self.model,
      deployment_name=self.deployment_name,
      callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
      streaming=True
    )

  def __call__(self, prompt, *args: Any, **kwds: Any) -> Any:

    template = f"""
      you know about the following list of llm use case archetypes:
      {st.session_state.archetypes}

      Here's a LLM use case.
      1. Categorize the use case based on the provided archetypes. If
      a use case cannot be categorized, create a new archetype. Only do that,
      if absolutely necessary.
      2. Briefly describe its technical implementation
      by naming required components, examplary products and technologies,
      and how the are used to implement the use case

      LLM Use Case:
      {prompt}

      Break your answer down into several paragraphs.
      Use syntax highlighting for code snippets,
      and links to external resources.
      Use colored text or emojis to highlight important parts.

      OUTPUT Format mus be compliant with the Github-flavored Markdown.
      Syntax information can be found at: https://github.github.com/gfm.
      This also supports:
      Emoji shortcodes, such as :+1: and :sunglasses:. For a list of all supported codes, see https://share.streamlit.io/streamlit/emoji-shortcodes.
      LaTeX expressions, by wrapping them in "$" or "$$" (the "$$" must be on their own lines). Supported LaTeX functions are listed at https://katex.org/docs/supported.html.
      Colored text, using the syntax :color[text to be colored], where color needs to be replaced with any of the following supported colors: blue, green, orange, red, violet, gray/grey, rainbow.
    """

    return self.llm([HumanMessage(content=template)]).content
