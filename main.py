import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = ""https://divan.ru"
driver.get(url)
time.sleep(3)