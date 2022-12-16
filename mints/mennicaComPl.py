from selenium import webdriver
from selenium.webdriver.common.by import By

def mennicaComPl():
    #open session by Driver_manager
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install))
    driver = webdriver.Chrome()

    #open URL
    driver.get("https://inwestycje.mennica.com.pl/produkty-inwestycyjne/srebro/srebrne-monety-bulionowe/")

    # wait till open 
    driver.implicitly_wait(15)

    names = driver.find_elements(By.XPATH, '//h2[@class="product-name"]') # find names of cluster by XPATH
    prices = driver.find_elements(By.XPATH, '//div[@class="price-box"]') #find prices of cluster bt XPATH

    results = []

    for x in range(len(names)):
        results.append({
                'name': names[x].text,
                'price': prices[x].text
            })

    #coin_names = []
    #for c in range(len(names)):
    #    coin_names.append(names[c].text)
    #    print(coin_names[c])

    #coin_prices = []
    #for p in range(len(prices)):
    #    coin_prices.append(prices[p].text)
    #    print(coin_prices[p])

    driver.quit()

    return results