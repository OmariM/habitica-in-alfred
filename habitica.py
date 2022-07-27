import request, json
from enum import Enum

## Enums
class Attribute(Enum):
        STR = 'str'
        INT = 'int'
        PER = 'per'
        CON = 'con'

class Priority(Enum):
        TRIVIAL = 0.1
        EASY = 1
        MEDIUM = 1.5
        HARD = 2

class Frequency(Enum):
        DAILY = 'daily'
        WEEKLY = 'weekly'
        MONTHLY = 'monthly'
        YEARLY = 'yearly'

## Networking Constants

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
# TODO: make this persistent in alfred
tags_dict = {
    'work': 'ff6be87c-6b82-42e2-90e5-e959c729c86b'
}
## Make task class


## Make user class

## Make subtask class
