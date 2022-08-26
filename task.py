import json
from dataclasses import dataclass

@dataclass
class Task:
    text: str
    type: str = 'todo'
    _id: str = None

    def to_json(self) -> str:
        return json.dumps(self, default=lambda x: {k:v for (k,v) in x.__dict__.items() if v is not None})

    def from_dict(task_dict):
        return Task(task_dict['text'],
                    task_dict['type'],
                    task_dict['_id'])

    def to_alfred_list_item(self, arg = None):
        return {
            'title': self.text,
            'subtitle':'select to complete',
            'arg': arg if arg is not None else self.to_json(),
            'autocomplete': self.text
        }
