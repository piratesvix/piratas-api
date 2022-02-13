# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

url = "www.google.com"

option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)


driver.get(url)
#driver.implicitly_wait(10)  # in seconds

language = driver.find_element_by_css_selector("#SIvCob > a")
language = language.text

print(language)
driver.quit()