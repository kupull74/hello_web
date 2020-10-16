import os 
os.getcwd()
import time

import requests
from bs4 import BeautifulSoup
#from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
import wget
import urllib.request

driver = webdriver.Chrome("/home/jerry/Documents/Develop/chromedriver")
driver.get("https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do;jsessionid=KV7jMa7yvwa8InddqpDOrg4h54vcVDsxuOW3htTMnD2C12yaVHM6aHMV7DNhEvIO.frswas01_servlet_engine5")

#산 이름 완료 
# for page in range(1,11):   #숫자 수정
#    raw = requests.get("http://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mntIndex=" + str(page * 1)).text
#    html = BeautifulSoup(raw, 'lxml')
#    Mnames = html.select('div.list_info > strong ') 
#    for Mname in Mnames:
#        print(Mname.text)

#노가다의 산물들       
#txt > ul > li:nth-child(2) > a > div > div.list_info > ul > li:nth-child(1) > span:nth-child(2)
#txt > ul > li:nth-child(84) > a > div > div.thumb > img
#txt > ul > li:nth-child(84) > a > div > div.thumb > img


#높이 완료
# for page in range(1,11):   #숫자 수정
#    raw = requests.get("http://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mntIndex=" + str(page * 1)).text
#    html = BeautifulSoup(raw, 'lxml')
#    heights = html.select('li:nth-child(1) > span:nth-child(2)') 
#    for height in heights:
#        print(height.text)

#이미지
# for page in range(1,11):   #숫자 수정
#    raw = requests.get("http://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mntIndex=" + str(page * 1)).text
#    html = BeautifulSoup(raw, 'lxml')
#    heights = html.select('img.autosize') 
#    for height in heights:
#        print(height)



# 이미지 성공

# driver.find_element_by_xpath('//*[@id="mntUnit"]/option[5]').click() 
# driver.find_element_by_xpath('//*[@id="txt"]/form/div[2]/div[2]/button').click()

# elements=driver.find_elements_by_css_selector(".autosize") #.get_attribute("src")
# count = 1 
# for element in elements:
#     #print(element)
#     count = count + 1
#     imgs = element.get_attribute("src")
#     urllib.request.urlretrieve(imgs, str(count) + ".jpg")


# 산 간결설명
# #//*[@id="txt"]/ul/li[1]/a/div/div[1]/img
driver.find_element_by_xpath('//*[@id="txt"]/ul/li[1]/a/div/div[1]/img').click() 
elements=driver.find_elements_by_tag_name('#txt > h4')
for element in elements:
    print(element.text.lstrip().split("-")[1])

# down_path = '/home/jerry/Documents/Develop/pictures/'
# for element in elements:
#     src = element.get_attribute('src')
# img_txt = src.split('/')[-1]
# image_name=down_path+img_txt
# wget.download(url=src, out=image_name)

driver.close()

#1번째 이미지
#https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mn=NKFS_03_01_12
#2번째 이미지
#/kfsweb/cmm/fms/FileDown.do?atchFileId=FILE_000000000424055&fileSn=1&thumbYn=Y
#/kfsweb/cmm/fms/FileDown.do?atchFileId=FILE_000000000424375&fileSn=1&thumbYn=Y
#/kfsweb/cmm/fms/FileDown.do?atchFileId=FILE_000000000423563&fileSn=1&thumbYn=Y
#/kfsweb/cmm/fms/FileDown.do?atchFileId=FILE_000000000423564&fileSn=1&thumbYn=Y
#/kfsweb/cmm/fms/FileDown.do?atchFileId=FILE_000000000423872&fileSn=1&thumbYn=Y