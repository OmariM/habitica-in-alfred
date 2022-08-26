import sys, json
import alfredhelper

task_json = ' '.join(sys.argv[1:])
alfredhelper.score_task(task_json)
