import os 
os.getcwd()
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='/home/jerry/Documents/Develop/chromedriver')
import wget
import urllib.request
url='https://www.google.com/search?q=%EB%90%9C%EC%9E%A5%EC%B0%8C%EA%B2%8C&tbm=isch&ved=2ahUKEwie1q_0xczsAhUG6ZQKHYlzDmQQ2-cCegQIABAA&oq=%EB%90%9C%EC%9E%A5%EC%B0%8C%EA%B2%8C&gs_lcp=CgNpbWcQAzICCAAyBggAEAoQGDIGCAAQChAYMgYIABAKEBgyBAgAEBgyBggAEAoQGDIGCAAQChAYMgYIABAKEBhQwaQcWJupHGC1rBxoAXAAeACAAcIBiAHKA5IBAzAuM5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=PMKTX57ID4bS0wSJ57mgBg&bih=936&biw=916'
driver.get(url=url)

#elements=driver.find_elements(By.XPATH, '//img[@class="search-product-wrap-img"]')
elements=driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
down_path = '/home/jerry/Documents/Develop/pictures/'
for element in elements:
    src = element.get_attribute('src')
#img_txt = src.split('/')[-1]
image_name=down_path #+img_txt
wget.download(url=src, out=image_name)

#islrg > div.islrc > div:nth-child(4) > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img

# 한글 지원
# 잘되네 well done
