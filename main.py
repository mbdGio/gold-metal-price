import requests
import os
import json
from bs4 import BeautifulSoup
from datetime import date

def main():
  URL = "https://mennicakapitalowa.pl/pol_m_Zloto_MONETY-BULIONOWE-131.html?filter_producer=&filter_traits%5B21%5D=&filter_traits%5B94%5D=&filter_traits%5B185%5D=&filter_traits%5B26%5D=20"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  all = soup.find(id="search")
  units = all.find_all("div", class_="product_wrapper")

  data = {}
  data['kapitalowa'] = []

  for unit in units:
    name = unit.find("a", class_="product-name").text.strip()
    price = unit.find("span", class_="price").text.strip()
    data['kapitalowa'].append({
      'name': name,
      'price': price
    })

  today = date.today()
  d1 = today.strftime("%Y-%m-%d")
  name = "./results/" + str(d1) + ".json"

  with open(name, 'w') as outfile:
    json.dump(data, outfile)

if __name__ == "__main__":
  main()
