import sys
from enum import Enum

args = sys.argv[1:]

################################ FORMAT ###################################
#                                                                         #
# name of task | tag1, tag2, ...,tagN | -subtask1 -subtask2 ... -subtaskN #
#                                                                         #
###########################################################################

input_string = args[0]
input_list = args[0].split('|')
input_type = 0

task_name = input_list[0]
tags = ''
subtasks = ''

if input_string.count('|') is 0:
    input_type = 4
elif input_string.count('|') is 1:
    if '-' in input_list[1]:
        input_type = 5
        subtasks = input_list[1]
    else:
        input_type = 6
        tags = input_list[1]
else:
    input_type = 7
    task_name, tags, subtasks = input_list[:3]

def split_to_strings(items_string, delimiter):
    return ' '.join([f'\"{item.strip()}\"' for item in items_string.split(delimiter)])


task_string = f'\"{task_name.strip()}\"'

if input_type//2 % 2 == 1:
    task_string = task_string + f' -t {split_to_strings(tags.strip(), ",")}'

if input_type % 2 == 1:
    task_string = task_string + f' --checklist {split_to_strings(subtasks.strip()[1:], "-")}'

sys.stdout.write(task_string)


