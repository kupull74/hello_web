import time

#import requests
#from bs4 import BeautifulSoup
#from pymongo import MongoClient
from selenium import webdriver

driver = webdriver.Chrome("/home/jerry/Documents/Develop/chromedriver")
driver.get("https://www.work.go.kr/empInfo/indRev/indRevMain.do")

# url = "https://www.work.go.kr/empInfo/indRev/indRevMain.do"
# res = requests.get(url, verify=False)
# soup = BeautifulSoup(res.content, features='lxml')


# def DBinsert(data):
#     db_url = 'mongodb://127.0.0.1:27017/'

#     with MongoClient(db_url) as client:
#         kwdb = client['kwork']
       
#         infor = kwdb.kwdbzips.insert_one(data)


#회사명 완료
# cp_list = [cors.text for cors in driver.find_elements_by_xpath("//a[@class='cp_name']")]
# print(cp_list)

#list1 > td:nth-child(3) > div > div > a

#채용공고명 완료
# ti_list = [titles.text for titles in driver.find_elements_by_tag_name("td:nth-child(3) > div > div > a")]
# print(ti_list)

#담당업무
#jobContLine1
dutes_list = [dutes.text for dutes in driver.find_elements_by_css_selector("td > div > div > p")]
print(dutes_list)

# def kwdb():

# for cate, term, title, li11_text, li22_text, li33_text in zip(cates, terms, titles, li1_text, li2_text, li3_text):
#     #print(cate.text, term.text, title.text, li1_text, li2_text, li3_text)


#     data = {'Category':cate.text, 'Term':term.text, 'Title':title.text.strip(), 'sorting':li11_text, 'Company':li22_text, 'Due':li33_text}
#     print(data)
#     #DBinsert(data)

# if __name__ == "__main__":
#     kwdb()
driver.close()
