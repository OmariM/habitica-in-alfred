import json, sys, requests
import networkhandler
from task import Task, ChecklistItem

def create_task(task_name) -> str:
    response = networkhandler.create_task(task_name)
    notif_string = f'task \'{task_name}\' created' if response.status_code == requests.codes.created else f'{response.status_code} Error\n{response.reason}'
    sys.stderr.write(response.text)
    sys.stdout.write(notif_string)

def score_task(task_json) -> str:
    task = Task.from_dict(json.loads(task_json))
    response = networkhandler.score_task(task)
    notif_string = f'marked \"{task.text}\" as complete'
    sys.stderr.write(response.text)
    sys.stdout.write(notif_string)

def get_tasks() -> str:
    task_list = networkhandler.get_tasks()
    alfred_items = [task.to_alfred_list_item() for task in task_list]
    alfred_response = json.dumps({'items': alfred_items})
    sys.stdout.write(alfred_response)

def get_tasks_to_add_checklist_item(item_name) -> str:
    item = ChecklistItem(item_name)
    task_list = networkhandler.get_tasks()
    alfred_items = [task.to_alfred_list_item(json.dumps({'item': item.to_json(), 'task': task.to_json()})) for task in task_list]
    alfred_response = json.dumps({'items': alfred_items})
    sys.stdout.write(alfred_response)

def add_checklist_item_to_task(item_json, task_json) -> str:
    item = ChecklistItem.from_dict(json.loads(item_json))
    task = Task.from_dict(json.loads(task_json))
    response = networkhandler.add_checklist_item_to_task(item, task)
    notif_string = f'added \"{item.text}\" to \"{task.text}\"'
    sys.stderr.write(response.text)
    sys.stdout.write(notif_string)
