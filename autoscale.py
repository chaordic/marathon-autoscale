import json
import math
import sys
import time

#useful endpoints
# http://TASK_HOST:5051/monitor/statistics.json
# http://MARATHON_HOST:8080/v2/apps
# http://MARATHON_HOST:8080/v2/apps/{app_id}

def get_app_ids():
  pass

def get_app_memthreshold(app_id):
  pass

def get_tasks(app_id):
  # return a dict task_id=>host
  pass

def get_task_stats(task_id, host):
  pass

def get_memusage(stats):
  pass

def scale_app(app_id):
  pass

def timer(delay_in_secs):
  pass

if __name__ == "__main__":
  print "Starting Marathon AutoScale v0.1"
  marathon_host = sys.argv[1]
  delay_in_secs = int(sys.argv[2])

  while True:
    app_ids = get_app_ids()

    for app_id in app_ids:
      mem_threshold = get_app_memthreshold(app_id)
      tasks = get_tasks(app_id)

      mem_usages = []

      for task_id, host in tasks:
        stats = get_task_stats(task_id, host)
        mem_usage = get_memusage(stats)
        mem_usages.append(mem_usage)

      if float(sum(mem_usages)) / len(mem_usages) > mem_threshold:
        scale_app(app_id)

    timer(delay_in_secs)









