import os 
os.getcwd()
import time

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
#from selenium import webdriver

# driver = webdriver.Chrome("/home/jerry/Documents/Develop/chromedriver")
# driver.get("https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A")

url = "https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A"
res = requests.get(url=url)
soup = BeautifulSoup(res.content, features='lxml')


def DBinsert(data):
    db_url = 'mongodb://127.0.0.1:27017/'

    with MongoClient(db_url) as client:
        kdb = client['kstartup']
       
        infor = kdb.kdbCollection.insert_one(data)



# contents = soup.select("#liArea0")
# for content in contents:
#     print(content.text.split('\n'))

#liArea0 > ul > li:nth-child(1)
#liArea1 > ul > li:nth-child(2)
#liArea0 > ul > li:nth-child(3)

# categorys = soup.select("ul > li > h4")
# for category in categorys:
#     print(category.text)
#liArea0 > h4 > a


#기간 완료
# for i in range(1, 10):

#     terms = soup.select(f'h4 > span.ann_list_day0{i}')
#     for term in terms:
#         print(term.text)


def kdb():

    #기간 진배꺼
    terms = soup.select('h4 > span[class*="ann_list_day"]')
    # for term in terms:
    #     print(term.text)



    #카테고리 완료
    # for i in range(1, 10):
    #     cates = soup.select(f'h4 > span.ann_list_group0{i}')
    #     for cate in cates:
    #         print(cate.text)


    #카테고리 진배꺼
    cates = soup.select('h4 > span[class*="ann_list_group"]')
    # for cate in cates:
    #     print(cate.text)


    #liArea0 > h4 > span.ann_list_group05


    #분류완료
    # for i in range(1, 171):
    #     sortings = soup.select(f'#liArea{i} > ul > li:nth-child(1)')
    #     #print(dues)
    #     for sorting in sortings:
    #         print(sorting.text)




    #기관완료
    # for i in range(1, 171):
    #     comps = soup.select(f'#liArea{i} > ul > li:nth-child(2)')
        #print(dues)
        # for comp in comps:
        #     print(comp.text)



    #기한완료
    # for i in range(1, 171):
    #     dues = soup.select(f'#liArea{i} > ul > li:nth-child(3)')
        #print(dues)
        # for due in dues:
        #     print(due.text)



    #li들 뽑아내기....진배옹의 가르침
    li1_text, li2_text, li3_text= [], [], []
    ul_tags = soup.find_all('ul', class_='ann_list_info m0')
    for ul in ul_tags:
        li_tags = []
        for li in ul.find_all('li'):
            li_tags.append(li.text)
        li1_text.append(li_tags[0])
        li2_text.append(li_tags[1])
        li3_text.append(li_tags[2].split()[1])
    #print(li1_text)


    #타이틀 완료
    titles= soup.select("li > h4 > a")
    # for title in titles:
    #     print(title.text)


    #liArea0 > h4 > a
    #liArea0 > h4 > *span.ann_list_group
    #<span class="ann_list_day05">마감2일전</span>
    #liArea0 > h4 > *span.ann_list_day


    # caterms= soup.select("li > h4 > span")
    # for caterm in caterms:
    #     # print(caterm)
    #     print(caterm.text.split('\n'))
    #ann_list_info m0

    # dues = soup.select(".ann_list_info > li+li)")
    # print(dues)
    # for due in dues:
    #     print(due.text)

    # dues = soup.select(".ann_list_info li+li")
    # for due in dues:
    #     print(due.text)

    # dues = soup.select(".ann_list_info li+li+li")
    # for due in dues:
    #     print(due.text)


    # titles= soup.select("#liArea0")
    # for title in titles:
    #     print(title.text.split('\n')[6].strip())

    # sortings = soup.select("#liArea0")
    # for sorting in sortings:
    #     print(sorting.text.split('\n')[13].strip())

    # companys = soup.select("#liArea0")
    # for company in companys:
    #     print(company.text.split('\n')[14].strip())

    # dues = soup.select("#liArea0")
    # for due in dues:
    #     print(due.text.split('\n')[15].strip())

    # for cate, term, sorting, title, comp, due in zip(cates, terms, sortings, titles, comps, dues ):
    #         print(cate.text, term.text, sorting.text, title.text, comp.text, due.text)



    for cate, term, title, li11_text, li22_text, li33_text in zip(cates, terms, titles, li1_text, li2_text, li3_text):
        #print(cate.text, term.text, title.text, li1_text, li2_text, li3_text)


        data = {'Category':cate.text, 'Term':term.text, 'Title':title.text.strip(), 'sorting':li11_text, 'Company':li22_text, 'Due':li33_text}
        print(data)
        DBinsert(data)




# driver = webdriver.Chrome("/home/jerry/Documents/Develop/chromedriver")
# driver.get("https://www.k-startup.go.kr/common/announcement/announcementList.do?mid=30004&bid=701&searchAppAt=A")
#     #webelement = driver.find_element_CSS_SELECTOR(), '[name="q"]')
#     #elements = driver.find_elements('a')

#elem = driver.find_elements_by_tag_name("Li")
#teme = elem.find_elements_by_tag_name("Li").text
#elements = driver.find_elements(By.XPATH, '//a[@href]')
#attr = driver.find_elements_by_xpath('//a[@href]')
#attr = driver.find_elements_by_id("")
#attr = driver.find_element_by_class_name("ann_list")
#uls = attr.find_element_by_tag_name('ul')






# afind = driver.find_element_by_class_name("btn_listAll")
# afind.click()

#time.sleep(5)
#driver.close()

if __name__ == "__main__":
    kdb()
