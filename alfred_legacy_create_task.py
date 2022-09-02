import sys, requests
from enum import Enum
from tags import tags_dict
from constants import auth_dict

args = sys.argv[1:]

################################ FORMAT ###################################
#                                                                         #
# name of task | tag1, tag2, ...,tagN | -subtask1 -subtask2 ... -subtaskN #
#                                                                         #
###########################################################################

input_string = args[0]
input_list = args[0].split('|')
input_type = 0

sys.stderr.write(f"\n list: {input_list} \n")
task_name = input_list[0]

sys.stderr.write(f"\n task_name: {task_name} \n")

tags = ''
subtasks = ''

if input_string.count('|') == 0:
    input_type = 4
elif input_string.count('|') == 1:
    if '-' in input_list[1]:
        input_type = 5
        subtasks = input_list[1]
        sys.stderr.write(f"\n task_name: {task_name} \n")
        sys.stderr.write(f"\n subtasks: {subtasks} \n")
    else:
        input_type = 6
        tags = input_list[1]
else:
    input_type = 7
    task_name, tags, subtasks = input_list[:3]

def split_to_strings(items_string, delimiter):
    return ' '.join([f'\"{item.strip()}\"' for item in items_string.split(delimiter)])

task_string = f'\"{task_name.strip()}\"'

task = {
    'text': task_string,
    'type': 'todo',
} 

if input_type//2 % 2 == 1:
    task['tags'] = [tags_dict[tag] for tag in split_to_strings(tags.strip(), ",")] 


if input_type % 2 == 1:
    task['checklist'] = [{'text': subtask} for subtask in subtasks.strip()[1:].split("-")]
    sys.stderr.write(f'\n checklist: {task["checklist"]} \n')

response = requests.post('https://habitica.com/api/v3/tasks/user', headers=auth_dict, json=task)

# build output
notif_string = f'task \'{task_name}\' created' if response.status_code == requests.codes.created else f'{response.status_code} Error\n{response.reason}'

sys.stdout.write(task_string)