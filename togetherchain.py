import os
import logging
import together
from langchain.llms.base import LLM
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)

class TogetherLLM(LLM):
    model: str = "togethercomputer/llama-2-7b-chat"
    together_api_key: str = os.environ["TOGETHER_API_KEY"]
    temperature: float = 0.7
    max_tokens: int = 512

    def __init__(self, model=None, max_tokens=None, temperature=None):
        if model:
            self.model = model
        if max_tokens:
            self.max_tokens = max_tokens
        if temperature:
            self.temperature = temperature

    @property
    def llm_type(self) -> str:
        return "together"

    def __call__(self, prompt: str, **kwargs) -> str:
        try:
            logging.info("Calling Together endpoint.")
            return self.make_api_call(prompt)
        except Exception as e:
            logging.error(f"Error in TogetherLLM call: {e}", exc_info=True)
            raise

    def make_api_call(self, prompt: str) -> str:
        together.api_key = self.together_api_key
        output = together.Complete.create(
            prompt,
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        logging.info("API call successful.")
        return output['output']['choices'][0]['text']

# Usage: 
# llm = TogetherLLM(
#     model="togethercomputer/llama-2-7b-chat",
#     max_tokens=256,
#     temperature=0.8
# )