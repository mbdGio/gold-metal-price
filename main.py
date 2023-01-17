from __future__ import unicode_literals
import json
from datetime import date
import os
import inspect
import mints
import codecs

def main():
  data = {}

  all = inspect.getmembers(mints, inspect.isfunction)
  for mint in all:
    data[mint[0]] = mint[1].__call__()

  today = date.today()
  d1 = today.strftime("%Y-%m-%d")
  if not os.path.exists('results'):
    os.makedirs('results')
  name = "./results/" + str(d1) + ".json"

  with codecs.open(name, 'w','utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)

if __name__ == "__main__":
  main()
