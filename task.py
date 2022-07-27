import json

class Task:
    def __init__(self, task_json):
        self._id = task_json['_id']
        self.text = task_json['text']
        self.tags = task_json['tags']
        self.checklist = task_json['checklist']
        self.json = json.dumps(task_json)

    def format_for_alfred(self):
        return {
            'title': self.text,
            'subtitle':'select to complete' if len(self.checklist) == 0 else 'show checklist',
            'arg': self.json,
            'autocomplete': self.text
        }
