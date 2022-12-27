import json, requests, sys
import urls, constants
from task import Task, ChecklistItem


def create_task(task_name):
    task = Task(task_name)
    task_dict = {k:v for (k,v) in task.__dict__.items() if v is not None}
    return requests.post(urls.GET_TASKS_URL, headers=constants.auth_dict, json=task_dict)

def score_task(task, direction='up'):
    return requests.post(urls.SCORE_TASK_URL.format(task._id, direction), headers=constants.auth_dict)

def get_tasks():
    tasks_response = requests.get(urls.GET_TASKS_URL, headers=constants.auth_dict, params={'type':'todos'})
    tasks_list = [Task.from_dict(t) for t in tasks_response.json()['data']]
    return tasks_list

def add_checklist_item_to_task(item, task):
    item_dict = {k:v for (k,v) in item.__dict__.items() if v is not None}
    return requests.post(urls.ADD_CHECKLIST_ITEM_URL.format(task._id), headers=constants.auth_dict, json=item_dict)
