import os 
os.getcwd()
import time
import selenium

from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/jerry/Documents/Develop/chromedriver')
print(type(driver), driver)

driver.get(url="https://www.google.com/")
print(type(driver.page_source), driver.page_source)