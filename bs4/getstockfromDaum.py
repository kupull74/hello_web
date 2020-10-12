import requests

url = 'http://finance.daum.net/api/market_index/days?page=1&perPage=100&market=KOSPI&pagination=true'
# Daum은 header 정보 확인해 임의의 header를 넣어줌
header = {'Referer' :'http://finance.daum.net/domestic/kospi',
          'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0...Safari/537.36'}
res = requests.get(url, headers = header) 		# headers 인자로 fake 접속하기

import json
rt_dict = json.loads(res.content)
print(rt_dict, rt_dict.keys())

import pandas as pd
print(rt_dict['data'][2])
df = pd.DataFrame(rt_dict['data'])
print(df)

import time
url = 'https://finance.naver.com/?code={}&page={}'
for x in range(0, 500):
    time.sleep(10)
    print(url.format('000000', x))