import json, sys

commands = [
    {
        'title': 'Create',
        'subtitle': 'create todo',
        'arg': 'create',
        'autocomplete': 'create'
    },
    {
        'title': 'Tasks',
        'subtitle': 'show tasks',
        'arg': 'tasks',
        'autocomplete': 'tasks'
    }
]

sys.stdout.write(json.dumps({'items': commands}))
