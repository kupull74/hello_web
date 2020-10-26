import os 
os.getcwd()
import time

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
import wget
import urllib.request
import json

#디비 함수 만들기
def DBinsert(data):
    db_url = 'mongodb://192.168.0.134:8088/'

    with MongoClient(db_url) as client:
        mtdb = client['mountaindb']
       
        infor = mtdb.mtdbColl.insert_one(data)


#100대 명산 100 한화면 출력 페이지 
# https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mntIndex=1&searchMnt=&searchCnd=&mn=NKFS_03_01_12&orgId=&mntUnit=100



# driver = webdriver.Chrome("/home/jerry/Documents/Develop/chromedriver")
# driver.get("https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mntIndex=1&searchMnt=&searchCnd=&mn=NKFS_03_01_12&orgId=&mntUnit=100")

url = "https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mntIndex=1&searchMnt=&searchCnd=&mn=NKFS_03_01_12&orgId=&mntUnit=100"
res = requests.get(url=url)
soup = BeautifulSoup(res.content, features='lxml')



mnames = []
#산 이름 non for문 ()안 산 이름 제거하기 성공!!
m_names = soup.select('div.list_info > strong ') 
for m_name in m_names:
    a = m_name.text[0:4].split("(")[0]
    #print(a)
    mnames.append(a)
for mname in mnames:
    print(mname)

    

#높이 non for문
mheights = []
m_heights = soup.select('li:nth-child(1) > span:nth-child(2)') 
for m_height in m_heights:
    mheights.append(m_height.text)
    for mheight in mheights:
        print(mheight)




# 이미지 성공
# driver.find_element_by_xpath('//*[@id="mntUnit"]/option[5]').click() 
# driver.find_element_by_xpath('//*[@id="txt"]/form/div[2]/div[2]/button').click()

# m_imgs=driver.find_elements_by_css_selector(".autosize") #.get_attribute("src")
# count = 1 
# for m_img in m_imgs:
#     #print(m_imgs)
#     count = count + 1
#     imgs = m_img.get_attribute("src")
#     urllib.request.urlretrieve(imgs, str(count) + ".jpg")





mbriefs = []
#산 간결설명 성공
briefs = soup.select('#txt > ul > li > a')
#txt > ul > li > a
#txt > ul > li:nth-child(2) > a 
for brief in briefs:
    link = brief['href']
    mlink = "https://forest.go.kr/" + link
    #print(mlink)
    url = mlink
    res = requests.get(url=url)
    soup = BeautifulSoup(res.content, features='lxml')
    m_briefs = soup.select('#txt > h4')
    for m_brief in m_briefs:
        if "-" in m_brief.text:
            comm = m_brief.text.strip().split("-")[1]
        else:
            comm = ""    
        #print(comm)
        mbriefs.append(comm)
        print(comm)


#날씨설명 성공!!(아씨ㅡㅜ)

from urllib.request import urlopen, Request
import urllib
import bs4

mweathers = []

locations = [m.text[0:4].split("(")[0] for m in m_names]

for location in locations:
    enc_location = urllib.parse.quote(location + '+날씨')

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ enc_location


    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'lxml')

    #m_weathers = (' 오늘 ' + location + ' ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도,' + '' + ' 날씨는 ' + soup.find('ul', class_='info_list').find('p', class_='cast_txt').text + '')
    m_weathers = (location + ' ' + soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text + '도,' + '' + ' 날씨는 ' + soup.find('ul', class_='info_list').find('p', class_='cast_txt').text + '')
    #print(m_weathers)
    mweathers.append(m_weathers)
    for mweather in mweathers: 
        print(mweather)

#링크넣기 
from bs4 import BeautifulSoup
url = "https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do?mntIndex=1&searchMnt=&searchCnd=&mn=NKFS_03_01_12&orgId=&mntUnit=100"
res = requests.get(url=url)
soup = BeautifulSoup(res.content, features='lxml')     

m_links = soup.select('#txt > ul > li > a')
for m_link in m_links:
    alink = m_link['href']
    mlink = "https://forest.go.kr" + alink
    print(mlink)



#for문 돌려서 몽고db에 넣기


# for mname, mheight, mbrief, mweather, m_link in zip(mnames, mheights, mbriefs, mweathers, m_links):
#     alink = m_link['href']
#     mlink = "https://forest.go.kr" + alink
#     data = {'M_name':mname, 'M_height':mheight, 'M_brief':mbrief, 'M_weather':mweather, 'M_link':mlink}
#     #print(data)
#     DBinsert(data)
#     #'M_brief':mbrief, 'M_weather':mweather,


mnum = 0

for mname, mheight, mbrief, mweather, m_link in zip(mnames, mheights, mbriefs, mweathers, m_links):
    mnum = mnum + 1
    print(mnum)

    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    #Host: dapi.kakao.com
    h = {"Authorization": "KakaoAK ea6791d8e5bb4b2a00e58692de73a617"}
    #address_name,&x={lon}&y={lat}}
    p = {"query":mname}
    res = requests.get(url = url, params= p, headers = h)
    # print(res.status_code)
    # print(res.content)

    #제이슨의 컨텐츠들 묶여있는 dic 보기
    #json.loads(res.content)[0]

    #첫번째 다큐먼트s 중에서 첫번째 내용들 선별해서 뽑아내기
    #json.loads(res.content)['documents'][0]
    maddress=(json.loads(res.content)['documents'][0]['address_name'])
    print(maddress)
    mlong=(json.loads(res.content)['documents'][0]['x'])
    print(mlong)
    mlat=(json.loads(res.content)['documents'][0]['y'])
    print(mlat)


    alink = m_link['href']
    mlink = "https://forest.go.kr" + alink
    data = {'M_num':mnum, 'M_name':mname, 'M_address':maddress, 'M_long':mlong, 'M_lat':mlat, 'M_height':mheight, 'M_brief':mbrief, 'M_weather':mweather, 'M_link':mlink}
    #print(data)
    DBinsert(data)




#테스트용
# mnum = 0
# for mname, mheight, m_link in zip(mnames, mheights, m_links):
    
#     mnum = mnum + 1
#     print(mnum)
    
#     url = "https://dapi.kakao.com/v2/local/search/keyword.json"
#     #Host: dapi.kakao.com
#     h = {"Authorization": "KakaoAK ea6791d8e5bb4b2a00e58692de73a617"}
#     #address_name,&x={lon}&y={lat}}
#     p = {"query":mname}
#     res = requests.get(url = url, params= p, headers = h)
#     # print(res.status_code)
#     # print(res.content)

#     #제이슨의 컨텐츠들 묶여있는 dic 보기
#     #json.loads(res.content)[0]

#     #첫번째 다큐먼트s 중에서 첫번째 내용들 선별해서 뽑아내기
#     #json.loads(res.content)['documents'][0]
#     maddress=(json.loads(res.content)['documents'][0]['address_name'])
#     print(maddress)
#     mlong=(json.loads(res.content)['documents'][0]['x'])
#     print(mlong)
#     mlat=(json.loads(res.content)['documents'][0]['y'])
#     print(mlat)


#     alink = m_link['href']
#     mlink = "https://forest.go.kr" + alink
#     data = {'M_num':mnum, 'M_name':mname, 'M_address':maddress, 'M_long':mlong, 'M_lat':mlat, 'M_height':mheight, 'M_link':mlink}
#     #print(data)
#     DBinsert(data)