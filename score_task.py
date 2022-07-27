import sys, task

from task import Task 
from habitica_todo import score_task

task_json = ' '.join(sys.argv[1:])
task = Task(json.loads(task_json))
score_task(task)


