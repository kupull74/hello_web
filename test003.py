import os 
os.getcwd()
import time

import requests
from bs4 import BeautifulSoup
import json

"""
import os
import sys
import urllib.request
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
"""


url = 'https://openapi.naver.com/v1/search/news.json?query=스마트'
header = {'X-Naver-Client-Id':'Na5eYLwQeBl2vA7b8VFR', 'X-Naver-Client-Secret':'_A8eKNId8L'}
response = requests.get(url, headers = header)
response.status_code
rt_dict = json.loads(response.content)
print(rt_dict.keys())

import pandas as pd
print(pd.DataFrame(rt_dict['items']))
#print(pd.DataFrame(rt_dict['lastBuildDate']))