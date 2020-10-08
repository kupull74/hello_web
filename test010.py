import os 
os.getcwd()
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='/home/jerry/Documents/Develop/chromedriver')
import wget
import urllib.request
url='https://www.coupang.com/np/search?q=%EC%BB%B4%ED%93%A8%ED%84%B0'
driver.get(url=url)

elements=driver.find_elements(By.XPATH, '//img[@class="search-product-wrap-img"]')
down_path = '/home/jerry/Documents/Develop/pictures/'
for element in elements:
    src = element.get_attribute('src')
img_txt = src.split('/')[-1]
image_name=down_path+img_txt
wget.download(url=src, out=image_name)

# 한글 지원
# 잘되네 well done
