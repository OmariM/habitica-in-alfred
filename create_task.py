import json, sys

from task import Task
from habitica_todo import create_task



def string_to_json(arg):
    # format: "task_name | tag1, ..., tagN | -subtask1 .... - subtaskN

