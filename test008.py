import os 
os.getcwd()
#import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#Find Element From Elements

driver = webdriver.Chrome(executable_path='/home/jerry/Documents/Develop/chromedriver')

driver.get(url="https://search.daum.net/search?w=tot&q=%EB%94%A5%EB%9F%AC%EB%8B%9D")
elements = driver.find_elements(By.XPATH, '//a[@href]')
#print(elements)

for e in elements:
    if e !=None:
        print(type(e.text), repr(e.text))
