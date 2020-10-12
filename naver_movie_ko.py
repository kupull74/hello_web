import os 
os.getcwd()
import time

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


# url='https://go.drugbank.com/drugs?page={}'
# for x in range(0,2):
#     time.sleep(1)
#     print(url.format(x))<td class="ac num">17157284</td>

    

def DBinsert(data):
    db_url = 'mongodb://172.17.0.1:27017/'

    with MongoClient(db_url) as client:
        ndb = client['naversample']
       
        infor = ndb.ndbCollection.insert_one(data)
        # except Exception as e:
        #     print(e)

#idx1.text, ti.text, scores.text, contents.text, adates.text, nusers.text

"""
https://movie.naver.com/movie/point/af/list.nhn
- movie page
 
"""
def ndb():

    url = "https://movie.naver.com/movie/point/af/list.nhn?&page=1"
    res = requests.get(url=url)
    soup = BeautifulSoup(res.content, features='lxml')


    # #id lists
    idx = soup.select("td.ac")
    # for idx1 in idx:
    #     print(idx1.text)


    # #movie titles
    title = soup.select("a.movie.color_b")
    # for ti in title:
    #     print(ti.text)


    # #scores
    score = soup.select("div.list_netizen_score")
    # for scores in score:
    #     print(scores.text)

    # #contents
    content = soup.select("td.title")
    # for contents in content:
    #     print(contents.text.split('\n')[5].strip())

    # #dates
    adate = soup.select('td[class="num"]')
    # for adates in adate:
    #     print(adates.text[8:])

    # #userIDs
    nuser = soup.select('td[class="num"]')
    # for nusers in nuser:
    #     print(nusers.text[:8])

    for idx1, ti, scores, contents, adates, nusers in zip(idx, title, score, content, adate, nuser):
        # print(idx1.text, ti.text, scores.text, contents.text, adates.text, nusers.text)
        data = {'ID':idx1.text, 'level':ti.text, 'score':scores.text,'contents':contents.text,'date':adates.text,'user':nusers.text,}
        DBinsert(data)