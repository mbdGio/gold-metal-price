import json
from datetime import date
from mints import *

def main():
  data = {}
  data['kapitalowa'] = mennicaKapitalowa()

  today = date.today()
  d1 = today.strftime("%Y-%m-%d")
  name = "./results/" + str(d1) + ".json"

  with open(name, 'w') as outfile:
    json.dump(data, outfile)

if __name__ == "__main__":
  main()
