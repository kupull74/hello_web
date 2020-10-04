import os 
os.getcwd()
#import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#Find Element From Elements

driver = webdriver.Chrome(executable_path='/home/jerry/Documents/Develop/chromedriver')

driver.get(url="https://www.google.com/search?q=webdriver")
elements = driver.find_elements(By.XPATH, '//a[@href]')
#print(elements)

for e in elements:
    if e !=None:
        print(type(e.text), repr(e.text))
