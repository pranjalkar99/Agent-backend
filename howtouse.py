"""Usage instructions"""
from graphs.main_graph import lesson_graph
from test_document import content
from pprint import pprint

state_input = {
    "document": content,
    "user_proficiency": "beginner"
}

output = lesson_graph.invoke(state_input)
# Huge output as it contains nptel transcript, output this only if you want to inspect the full state
# print('STATE')
# pprint(output)
# print('\n\n')

print("Lesson Structure")
pprint(output.get('lesson_planner_obj'))
print("\n\n")

print("Lesson Generation")
pprint(output.get('lesson_generator_obj').content)