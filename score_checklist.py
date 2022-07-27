import sys, json

from task import Task
from habitica_todo import score_checklist_task

response_json = json.loads(' '.join(sys.argv[1:]))
task = Task(json.loads(response_json['task']))
checklist_item_id = response_json['checklist_item_id']

score_checklist_task(task, checklist_item_id)
