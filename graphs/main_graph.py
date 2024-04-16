from typing import TypedDict, Any
from langgraph.graph import StateGraph, END
from langchain_core.pydantic_v1 import Field
from langchain_core.documents import Document

from agents.lesson_planner import lesson_planner_runnable, LessonStructure
from agents.lesson_generator import lesson_generator_runnable

class AgentState(TypedDict):
    # Document Object
    document: Document = Field(..., description="The document to be processed")
    lesson_planner_obj: LessonStructure
    lesson_generator_obj: Any # not sure for now
    user_proficiency: str

def call_lesson_planner(state):
    inputs = {
        "document": state["document"],
        "user_proficiency": state["user_proficiency"],
    }

    return {
        'lesson_planner_obj': lesson_planner_runnable.invoke(inputs)
    }
def call_lesson_generator(state):
    inputs = {
        "document": state["document"],
        "user_proficiency": state["user_proficiency"],
        "topics": state["lesson_planner_obj"].Topics
    }

    return {
        'lesson_generator_obj': lesson_generator_runnable.invoke(inputs)
    }

graph = StateGraph(AgentState)
graph.add_node('lesson_planner', call_lesson_planner)
graph.add_node('lesson_generator', call_lesson_generator)
graph.set_entry_point('lesson_planner')
graph.add_edge('lesson_planner', 'lesson_generator')
graph.add_edge('lesson_generator', END)
lesson_graph = graph.compile()