import sys, json
import alfredhelper
from task import ChecklistItem

item_name = ' '.join(sys.argv[1:])
alfredhelper.get_tasks_to_add_checklist_item(item_name)
