import os 
os.getcwd()
import time

import requests
from bs4 import BeautifulSoup
import json

"""
 {
        "id": 833,
        "name": "Ḩeşār-e Sefīd",
        "state": "",
        "country": "IR",
        "coord": {
            "lon": 47.159401,
            "lat": 34.330502
        }
  },   
"""


with open('city.list.json') as jdata:
    son_datas = json.load(jdata)
    #print(type(son_datas))
    #k=0
    #son_data1=(int(son_datas))

    #name=()
    # for son_data1 in son_datas:
    #     k=0   
    #     #print(son_data1.get("name"))
        
    #     while son_data1 <= 30:
    #          print(son_data1.get("name"))
    #          k+=1 
               
          
    #     #     break 

ns={}            
for ns in son_datas(range(0,31)):
    print(ns)


url = "http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=3aab6df08450a694b80018ccc7e86746"
res = requests.get(url=url)
#soup = BeautifulSoup(res.content, features='lxml')

# locations = soup.find_all('location')
# for location in locations:
#     print(location.find('city').text, ":", location.find('wf').text)
#ddsdsdsdsdsd

# locations = soup.select("item")

# for location in locations:
#     print(location.find("title").text, ('\n\n'), ":", location.find("wf").text)

# weathers = soup.select("weather")
# for weather in weathers :
#     print(weather[0])

rt_dicts = json.loads(res.content)
#print(rt_dicts, rt_dicts.keys())
# for rt_dict in rt_dicts:
#     print(rt_dict)

weather=rt_dicts["weather"][0]["main"], rt_dicts["weather"][0]["description"], rt_dicts["name"]
print(weather)