import sys
import requests
import json
import argparse
import asyncio
from task import Task

## Constants

# Networking
USER_ID = 'a7e29731-49ab-4a26-956f-ca3ba4cfb580'
API_TOKEN = 'c093efb2-4bca-45b6-9f76-ba8a25b9fdae'
CLIENT_HEADER = USER_ID + 'Testing'

GET_TASKS_URL = 'https://habitica.com/api/v3/tasks/user'
SCORE_TASK_URL = 'https://habitica.com/api/v3/tasks/{}/score/{}'
SCORE_CHECKLIST_ITEM_URL = 'https://habitica.com/api/v3/tasks/{}/checklist/{}/score'

auth_dict = {
	"x-api-user": USER_ID,
	"x-api-key": API_TOKEN,
	"x-client": CLIENT_HEADER
}

# Tags
tags_dict = {
    'work': 'ff6be87c-6b82-42e2-90e5-e959c729c86b'
}

## functions 
def get_tasks_for_alfred():
    tasks_response = requests.get(GET_TASKS_URL, headers=auth_dict, params={'type':'todos'}).json()
    tasks = [Task(task_json).format_for_alfred() for task_json in tasks_response['data']]
    alfred_response = json.dumps({'items': tasks})
    sys.stdout.write(alfred_response)

def get_checklist_from_task(task):
    checklist = [
            {
                'title': f'{"[x]" if checklist_item["completed"] else "[  ]"} {checklist_item["text"]}',
                'arg': json.dumps({'task': task.json, 'checklist_item_id': checklist_item['id']})
            } for checklist_item in task.checklist]
    checklist += [{'title': f'score \"{task.text}\"', 'arg': json.dumps({'task': task.json, 'uuid': 'UUID_SCORE_TASK'})}]
    alfred_response = json.dumps({'items': checklist})
    sys.stdout.write(alfred_response)

def score_checklist_task(task, checklist_item_id):
    score_response = requests.post(SCORE_CHECKLIST_ITEM_URL.format(task._id, checklist_item_id), headers=auth_dict)
    notif_string = f'marked item as complete'
    sys.stderr.write(score_response.text)
    sys.stdout.write(notif_string)

def score_task(task, direction='up'):
    score_response = requests.post(SCORE_TASK_URL.format(task._id, direction), headers=auth_dict)
    notif_string = f'marked \"{task.text}\" as complete'
    sys.stderr.write(score_response.text)
    sys.stdout.write(notif_string)

def create_task(task):
    response = requests.post('https://habitica.com/api/v3/tasks/user', headers=auth_dict, json=task)


def get_tags():
    return requests.get('https://habitica.com/api/v3/tags', headers=auth_dict).json()


## run the network request
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='get task name')
    parser.add_argument('task_name', type=str, help='name of the task')
    parser.add_argument('-t', '--tags', type=str, nargs='+', help='name of pre-existing tag')
    parser.add_argument('--checklist', type=str, nargs='+', help='checklist items')
    args = parser.parse_args()

    task_name = args.task_name
    tags = args.tags
    checklist = args.checklist


    task = {
	    'text': task_name,
	    'type': 'todo',
    } 

    if args.tags:
        task['tags'] = [tags_dict[tag] for tag in tags] 


    if args.checklist:
        task['checklist'] = [{'text': subtask} for subtask in checklist]

    response = requests.post('https://habitica.com/api/v3/tasks/user', headers=auth_dict, json=task)

    # build output
    notif_string = f'task \'{task_name}\' created' if response.status_code == requests.codes.created else f'{response.status_code} Error\n{response.reason}'  

    sys.stdout.write(notif_string)
