import os 
os.getcwd()
#import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#Find Element From Elements

driver = webdriver.Chrome(executable_path='/home/jerry/Documents/Develop/chromedriver')

driver.get(url="https://www.daum.net/")
elements = driver.find_elements(By.XPATH, '//span[@class]')
print(elements)

for e in elements:
    if e !=None:
        print(type(e.text), repr(e.text))
#<h3 class="tit_shopslot tit_event"><span class="ir_wa">인기기획전</span></h3>