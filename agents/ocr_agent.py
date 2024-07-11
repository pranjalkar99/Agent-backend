"""Lesson Generator Agent"""
import os
from typing import List
from init import initialize_env
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_together import Together
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from togetherchain import TogetherLLM
system_prompt_initial="""You are an expert interpreter. You are going to get ocr results from a document and you are expected to parse it properly and make sense of it.
If it doesnt make any sense, you may skip the part which doesnt make any sense.

Whenever You are invoked you do the following steps silently.
1. Read the document line by line and try to make the best sense out of it.
2. Understand each and every concept in the document in detail.

------------------DOCUMENT--------------------------
{document}
-----------------END OF DOCUMENT--------------------


I will tip you $20 if you are perfect, and I will fine you $40 if you miss any important information or change hallucinate up details.

Take a deep breath, think step by step, analyze the document and generate a lesson:
"""


prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt_initial),
    ]
)

initialize_env()

# llm = ChatOpenAI(
#     api_key=os.environ['OPENAI_API_KEY'], 
#     base_url=os.environ['OPENAI_API_BASE'],
#     model="gpt-4-turbo-2024-04-09",
#     streaming=True,
#     temperature=0.0,
# )
llm = TogetherLLM(
    together_api_key="6e5e02a2d3758839cc7e1bae11c6d4ec1f683744d1fbfcc01192336b7f0e8db4",
    model="meta-llama/Llama-3-8b-chat-hf",
    temperature=0,
    max_tokens=3500
)
llm = ChatGroq(model_name = "mixtral-8x7b-32768")

ocr_runnable = prompt | llm | StrOutputParser()