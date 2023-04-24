import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time

# TODO Read all 4,5k condo summaries to fetch deeper info.

def read_page_row(response):
    soup = BeautifulSoup(response, "html.parser")
    room_data = soup.findAll("div", {"class":"row teaser"})
    specifics_data = soup.findAll("div", {"class":"col-lg-3 col-sm-6 carac-container"})
    
    bedroom = ""
    bathroom = ""
    content = []

    content.append(soup.find("h2", itemprop="address").string)
    content.append(soup.find("span", id="BuyPrice").string)
    
    for value in specifics_data[1:3]:
        sub_value = value.select_one(".carac-value span")
        
        if sub_value:
            content.append(sub_value.string)

    for data in room_data:
        bathroom = data.find("div", {"class":"col-lg-3 col-sm-6 sdb"})
        bedroom = data.find("div", {"class":"col-lg-3 col-sm-6 cac"})
        rooms = data.find("div", {"class":"col-lg-3 col-sm-6 piece"})

        if bathroom:
            content.append(bathroom.string.strip())

        if bedroom:
            content.append(bedroom.string.strip())

        if rooms:
            content.append(rooms.string.strip())

    return content

option_argument = Options()
option_argument.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options = option_argument)
driver.get('https://www.centris.ca/en/condos~for-sale~montreal-verdun-ile-des-soeurs/20598619?view=Summary')

print(read_page_row(driver.page_source))

data = []
limit = 0
time.sleep(15)

#testing with limited fetching
while limit < 100:
    time.sleep(1)
    data.append(read_page_row(driver.page_source))

    try:
        driver.find_element(By.CLASS_NAME, "next").click()
    except ElementClickInterceptedException:
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "DialogInsightLightBoxCloseButton").click()

        print("Bye bye pop-up")
        time.sleep(2)

    limit += 1
    print(limit)

print(data, len(data), limit)

with open("output.csv", "w", encoding='utf-8') as txt_file:
    for line in data:
        txt_file.write(" ".join(line) + "\n")