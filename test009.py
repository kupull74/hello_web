import os 
os.getcwd()
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/home/jerry/Documents/Develop/chromedriver')

driver.get(url="https://www.google.com/")
from selenium.webdriver.common.keys import Keys

driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

Searchinput = driver.find_element(By.NAME, "q")
Searchinput.send_keys("selenium")

time.sleep(5)
Searchinput.clear()