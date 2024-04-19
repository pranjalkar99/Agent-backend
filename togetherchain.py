from typing import Any, List, Optional

from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from pydantic import Field, SecretStr

from together import Together


class TogetherLLM(LLM):
    model: str = Field(...,description="The model to use for the Together LLM.")
    together_api_key: str = Field(...,description="The API key for the Together API.")
    temperature: float = Field(..., description="The temperature to use for the Together LLM.")
    max_tokens: int = Field(..., description="The maximum number of tokens to generate for the Together LLM.")

    @property
    def _llm_type(self) -> str:
        return "together"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        
        try:
            client = Together(api_key=self.together_api_key)
            response = client.chat.completions.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as e:
            raise

        

# Usage: 
# llm = TogetherLLM(
#     model="togethercomputer/llama-2-7b-chat",
#     max_tokens=256,
#     temperature=0.8
# )