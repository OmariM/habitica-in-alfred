import sys, json
import alfredhelper

args = json.loads(' '.join(sys.argv[1:]))
item = args['item']
task = args['task']
alfredhelper.add_checklist_item_to_task(item, task)
