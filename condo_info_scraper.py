import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
import time

# TODO Read all 4,5k condo summaries to fetch deeper info.

def read_page_row(response):
    soup = BeautifulSoup(response, "html.parser")
    title_data = soup.findAll("div", {"class":"row"})
    room_data = soup.findAll("div", {"class":"row teaser"})
    specifics_data = soup.findAll("div", {"class":"col-lg-3 col-sm-6 carac-container"})
    
    content = []

    content.append(soup.find("h2", itemprop="address").string)
    content.append(soup.find("span", id="BuyPrice").string)
    
    for value in specifics_data[1:3]:
        content.append(value.select_one(".carac-value span").string)

    for data in room_data:
        content.append(data.find("div", {"class":"col-lg-3 col-sm-6 piece"}).string.strip())
        content.append(data.find("div", {"class":"col-lg-3 col-sm-6 cac"}).string.strip())
        content.append(data.find("div", {"class":"col-lg-3 col-sm-6 sdb"}).string.strip())
        
    return content

option_argument = Options()
option_argument.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options = option_argument)
driver.get('https://www.centris.ca/en/condos~for-sale~montreal-ville-marie/28624180?view=Summary')

print(read_page_row(driver.page_source))

""" data = []
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

np.savetxt('condo_price_data.csv', data, delimiter="\n", fmt="%s") """