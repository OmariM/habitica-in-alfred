import sys, json

from task import Task
from habitica_todo import get_checklist_from_task

task_json = ' '.join(sys.argv[1:])
task = Task(json.loads(task_json))
get_checklist_from_task(task)


