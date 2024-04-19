"""Lesson Planner Agent"""
import os
from typing import List
from init import initialize_env
# from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
# from langchain_together import Together
from langchain_groq import ChatGroq
from togetherchain import TogetherLLM

# you can use Internet search tool to find more information. Don't try to make up an answer.
system_prompt_initial="""You are a teacher with decades of knowledge in effective teaching methods. Your task is to create a lesson based on the contents of the given document that will engage and educate students about the key concepts.
When you recieve a document, you silently do the following steps:
1. Read the document thoroughly to understand the content and key points.
2. Identify the main topics and themes covered in the document.

Do not hallucinate up details, if you do not know something, dont reply with anything

Given below is a profile of the user and at what level they are expected to understand the lesson:
User proficiency: {user_proficiency}

------DOCUMENT------
Here is the given document:
{document}
------END OF DOCUMENT------


Please use the given format to structure your lessons:
-----FORMAT INSTRUCTIONS-----
{format_instructions}
-----END OF FORMAT INSTRUCTIONS-----
Its extremely important that you follow the specified format and do not deviate. 
I will tip you $20 if you are perfect, and I will fine you $40 if you miss any important information or change hallucinate up details.

Take a deep breath, think step by step, and then analyze the document:
"""

class LessonStructure(BaseModel):
    Title: str = Field(..., title="Title of the Lesson")
    LessonObjectives: List[str] = Field(..., title="Lesson Objectives and what will be achieved by the end of the lesson")
    Motivation: List[str] = Field(..., title="Why are we learning this? How does this apply to the real world? Why is this important?")
    Summary: str = Field(..., title="Summary of the Lesson")
    Topics: List[str] = Field(..., title="Topics covered in this lesson")
    # Search : bool = Field(..., title="Internet search tool, Do I have enough information to generate the lesson") 
    # SearchQuery : str = Field(..., title="Search Query for the internet search tool")


parser = PydanticOutputParser(pydantic_object=LessonStructure)
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt_initial),
    ]
).partial(format_instructions=parser.get_format_instructions())

initialize_env()
# LLM Which will drive this agent
# llm = ChatOpenAI(
#     api_key=os.environ['OPENAI_API_KEY'], 
#     base_url=os.environ['OPENAI_API_BASE'],
#     model="gpt-4-turbo-2024-04-09",
#     streaming=True,
#     temperature=0.0,
# )
llm = TogetherLLM(
    together_api_key="6e5e02a2d3758839cc7e1bae11c6d4ec1f683744d1fbfcc01192336b7f0e8db4",
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0,
    max_tokens=3500
)
# llm = ChatGroq(model_name = "mixtral-8x7b-32768")

lesson_planner_runnable = prompt | llm | parser