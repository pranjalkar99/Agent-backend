"""Quiz Agent"""
from typing import List

from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain_groq import ChatGroq

system_prompt_initial = """You are a quiz generation expert. Your task is to generate a quiz based on the contents of a given document.
You do not need to generate a lesson plan or lesson as it will be handled by different agents.
Whenever You are invoked you do the following steps silently.
1. Read the document line by line and understand its contents deeply.
2. Understand each and every concept in the document in detail.

\n\n------------------DOCUMENT--------------------------\n
{document}
\n-----------------END OF DOCUMENT--------------------\n


\n\n\nGiven below is a profile of the user and at what level they are expected to understand the quiz:
\nUser proficiency: {user_proficiency}


\n\n\nYou are expected to generate a quiz that is suitable for the user's proficiency level and tests their understanding of the concepts covered in the document. The quiz should be varied, engaging and should be able to accurately assess the student's understanding.

Please use the given format to structure your output:
-----FORMAT INSTRUCTIONS-----
{format_instructions}
-----END OF FORMAT INSTRUCTIONS-----

I will tip you $20 if you create a great quiz, and I will fine you $40 if you include any misleading or incorrect information.

\n\nTake a deep breath, think step by step, analyze the document and generate a quiz:"""


class Quiz(BaseModel):
    questions : List[str] = Field(
        description="The questions to be generated based on the passed documents."
    )
    answers: List[str] = Field(
        description="The answers to the questions you have generated."
    )
    reasoning: List[str] = Field(
        description="The reasoning behind the answers to the quiz questions."
    )



parser = PydanticOutputParser(pydantic_object=Quiz)

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt_initial),
    ]
).partial(format_instructions=parser.get_format_instructions())

# Choose the LLM that will drive the agent


llm = ChatGroq(model_name = "mixtral-8x7b-32768")

quiz_runnable = prompt | llm | parser
