import json
from datetime import date
import inspect
import mints

def main():
  data = {}

  all = inspect.getmembers(mints, inspect.isfunction)
  for mint in all:
    data[mint[0]] = mint[1].__call__()

  today = date.today()
  d1 = today.strftime("%Y-%m-%d")
  name = "./results/" + str(d1) + ".json"

  with open(name, 'w') as outfile:
    json.dump(data, outfile)

if __name__ == "__main__":
  main()
