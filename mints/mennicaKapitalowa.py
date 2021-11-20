import requests
from bs4 import BeautifulSoup

def mennicaKapitalowa():
  URL = "https://mennicakapitalowa.pl/pol_m_Zloto_MONETY-BULIONOWE-131.html?filter_producer=&filter_traits%5B21%5D=&filter_traits%5B94%5D=&filter_traits%5B185%5D=&filter_traits%5B26%5D=20"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  all = soup.find(id="search")
  units = all.find_all("div", class_="product_wrapper")

  res = []
  for unit in units:
    name = unit.find("a", class_="product-name").text.strip()
    price = unit.find("span", class_="price").text.strip()
    res.append({
      'name': name,
      'price': price
    })
  return res
