import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
import time

def read_page(response):
    soup = BeautifulSoup(response, "html.parser")
    data = []

    for price in soup.findAll("div", {"class":"price"}):
        data.append(price.select_one(".price span").string)

    return data


option_argument = Options()
option_argument.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options = option_argument)
driver.get('https://www.centris.ca/en/condos~for-sale~montreal-island?view=Thumbnail&uc=4')

data = []
limit = 0

#testing with limited fetching
while limit  < 227:
    try:
        time.sleep(1)
        data.extend(read_page(driver.page_source))
        driver.find_element("xpath", '//*[@id="divWrapperPager"]/ul/li[4]/a').click()

        limit += 1
    except ElementClickInterceptedException:
        time.sleep(2)
        driver.find_element("xpath", '/html/body/div/div/div[2]').click()
        print("Popup blocked")
        time.sleep(2)
    print(limit)

print(data, len(data), limit)

np.savetxt('condo_price_data.csv', data, delimiter="\n", fmt="%s")