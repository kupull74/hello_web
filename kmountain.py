import os 
os.getcwd()
import time

import requests
from bs4 import BeautifulSoup
#from pymongo import MongoClient
from selenium import webdriver

driver = webdriver.Chrome("/home/jerry/Documents/Develop/chromedriver")
driver.get("https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do;jsessionid=KV7jMa7yvwa8InddqpDOrg4h54vcVDsxuOW3htTMnD2C12yaVHM6aHMV7DNhEvIO.frswas01_servlet_engine5")

url = "https://www.forest.go.kr/kfsweb/kfi/kfs/foreston/main/contents/FmmntSrch/selectFmmntSrchList.do"
res = requests.get(url=url)
soup = BeautifulSoup(res.content, features='lxml')


# def DBinsert(data):
#     db_url = 'mongodb://127.0.0.1:27017/'

#     with MongoClient(db_url) as client:
#         kmdb = client['kmountain']
       
#         infor = kmdb.kmdbMountain.insert_one(data)




#def kmtdb():

# page in range(10):

# terms = soup.select('li > a > div > div.list_info > strong')
# for term in terms:
#     print(term.text)
#txt > ul > li:nth-child(1) > a > div > div.list_info > strong
#txt > ul > li:nth-child(20) > a > div > div.list_info

page_bar = driver.find_elements_by_css_selector("div.paginate > *")

    

    # for cate, term, title, li11_text, li22_text, li33_text in zip(cates, terms, titles, li1_text, li2_text, li3_text):
        #print(cate.text, term.text, title.text, li1_text, li2_text, li3_text)


        # data = {'Category':cate.text, 'Term':term.text, 'Title':title.text.strip(), 'sorting':li11_text, 'Company':li22_text, 'Due':li33_text}
        # print(data)
        # DBinsert(data)

#driver.close()


