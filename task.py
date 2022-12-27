import json
from dataclasses import dataclass

@dataclass
class ChecklistItem:
    text: str
    completed: bool = False
    _id: str = None

    # TODO: FIX
    def to_json(self) -> str:
        '''
        Returns a json representation of the non-None fields as a str
        '''
        return json.dumps(self, default=lambda x: {k:v for (k,v) in x.__dict__.items() if v is not None})

    def from_dict(checklist_item_dict):
        '''
        Creates a ChecklistItem object from a dictionary representation of a checklist item
        '''
        return ChecklistItem(checklist_item_dict['text'],
                             checklist_item_dict['completed'],
                             checklist_item_dict.setdefault('id', None))

    def to_alfred_list_item(self, arg = None):
        '''
        Returns a dictionary representation of an alfred list item for this checklist item

        Attributes:
            arg (str): the arg to be passed into the next workflow item when this list item is selected
        '''
        return {
            'title': f"[{' ' if self.completed else 'x'}] {self.text}",
            'subtitle': f"select to {'check' if self.completed else 'uncheck'}",
            'arg': arg if arg is not None else self.to_json(),
            'autocomplete': self.text
        }


@dataclass
class Task:
    '''
    A class to hold onto a task that can be sent to or retrieved from the server

    Attributes:
        text (str): the text of the task
        type (str): the type of task
        _id (str): the id of the task
        checklist (list): a list of checklist objects
        arg (str): the arg to be passed onto as the input in alfred
    '''
    text: str
    type: str = 'todo'
    _id: str = None
    checklist: [ChecklistItem] = None

    def __post_init__(self):
        self.checklist = [self.checklist] if self.checklist is not list and self.checklist is not None else self.checklist

    # TODO: FIX
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
                    task_dict.setdefault('_id', None),
                    task_dict.setdefault('checklist', None))

    def to_alfred_list_item(self, arg = None):
        '''
        Returns a dictionary representation of an alfred list item for this task

        Attributes:
            arg (str): the arg to be passed into the next workflow item when this list item is selected
        '''
        return {
            'title': self.text,
            'subtitle':'select to complete',
            'arg': self.to_json() if arg is None else arg,
            'autocomplete': self.text
        }
