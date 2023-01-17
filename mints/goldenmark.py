import requests
from bs4 import BeautifulSoup

def goldenmark():
  URL = "https://goldenmark.com/pl/zlote-monety-bulionowe"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  all = soup.find(id="js-product-list")
  all.find_all
  units = all.find_all("div", class_="product-description")
  res = []
  for unit in units:
    name = unit.find("h2", class_="h3 product-title").text.strip()
    priceInfo = str(unit.find("span", class_="price").text.strip())
    price = priceInfo
    if priceInfo is not None:
      price = priceInfo.replace('od', '')
      price = price.strip()
    res.append({
      'name': name,
      'price': price
    })
  return res

