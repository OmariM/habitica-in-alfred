import json
from dataclasses import dataclass

@dataclass
class Task:
    '''
    A class to hold onto a task that can be sent to or retrieved from the server

    Attributes:
        text (str): the text of the task
        type (str): the type of task
        _id (str): the id of the task
    '''
    text: str
    type: str = 'todo'
    _id: str = None

    def to_json(self) -> str:
        '''
        Returns a json representation of the non-None fields as a str
        '''
        return json.dumps(self, default=lambda x: {k:v for (k,v) in x.__dict__.items() if v is not None})

    def from_dict(task_dict):
        '''
        Creates a Task object from a dictionary representation of a task
        '''
        return Task(task_dict['text'],
                    task_dict['type'],
                    task_dict['_id'])

    def to_alfred_list_item(self, arg = None):
        '''
        Returns a dictionary representation of an alfred list item for this task

        Attributes:
            arg (str): the arg to be passed into the next workflow item when this list item is selected
        '''
        return {
            'title': self.text,
            'subtitle':'select to complete',
            'arg': arg if arg is not None else self.to_json(),
            'autocomplete': self.text
        }
