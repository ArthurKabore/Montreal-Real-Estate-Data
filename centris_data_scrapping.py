import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://www.centris.ca/en/condos~for-sale~montreal-island?view=Thumbnail&uc=4"

def read_page(response):
    soup = BeautifulSoup(response, "html.parser")

    for price in soup.findAll("div", {"class":"price"}):
        print(price)

driver = webdriver.Chrome()
driver.get('https://www.centris.ca/en/condos~for-sale~montreal-island?view=Thumbnail&uc=4')

while True:
    print("################################")

    read_page(driver.page_source)
    
    time.sleep(3)

    driver.find_element("xpath", '//*[@id="divWrapperPager"]/ul/li[4]/a').click()

    