import request, json

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

## Make task class

## instance variables



## Make 
