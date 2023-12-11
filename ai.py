from typing import Any, List, Mapping, Optional
import json
import requests
import streamlit as st

from langchain.llms.base import LLM
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManagerForLLMRun

class ExxetaAI(LLM):

    model: str

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        response = requests.request(
          "POST", f"https://ai.exxeta.com/api/azure/{self.model}/chatCompletion",
          headers={
            'Authorization': f'Bearer {st.session_state.api_token}',
            'Content-Type': 'application/json'
          },
          data=json.dumps({
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2500,
            "temperature": 0.1,
            "top_p": 0.95,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            #"stop": "string",
            "stream": False
          }))

        return json.loads(response.text).get("choices")[0].get("message").get("content")



    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model": self.model}
