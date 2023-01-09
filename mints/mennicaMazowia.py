import requests
from bs4 import BeautifulSoup

def mennicaMazowia():
  URL = "https://mennicamazovia.pl/pol_m_Zloto-Inwestycyjne_Zlote-Monety-165.html"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  all = soup.find(id="search")
  units = all.find_all("div", class_="product col-6 col-sm-4 col-md-3 pt-3 pb-md-3 mb-3 mb-sm-0")
  
  res = []
  for unit in units:
    name = unit.find("a", class_="product__name").text.strip()
    priceInfo = ""
    priceInfo = str(unit.find("strong", class_="price").text.strip())
    price = priceInfo.replace(' / szt. brutto', '')
    res.append({
      'name': name,
      'price': price
    })
  return res
