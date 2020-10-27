# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:20:26 2020

@author: Ezio Kevin
"""



import requests
from bs4 import BeautifulSoup
import time

#取得站點名稱

def getSoup(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'lxml')
        return soup
    
    return None

url='https://www.railway.gov.tw/tra-tip-web/tip'


#取得常用站點資料
soup=getSoup(url)
#print(soup)

lis=soup.find(id='cityHot').find_all('li')
#print(lis)

#test

#print(lis[0])


for li in lis:
    print(li.text)
    print(li.find('button').get('title'))

#print(lis[0])

#組成字典

station={}

for li in lis:
    print(li.text)
    print(li.find('button').get('title'))
    station[li.text]=li.find('button').get('title')
#print(station)


#推導式
station={li.text:li.find('button').get('title') for li in lis}
#print(station)

#函式化

def getStation(url):
    station={}
    soup=getSoup(url)    
    if soup!=None:    
        citys=soup.find(id='cityHot').find_all('li')
        for city in citys:
            name=city.find('button').text
            code=city.find('button')['title']

            station[name]=code
            
    return station

getStation(url)


#取得 request url and crsf code

main_url='https://www.railway.gov.tw'

api_url=soup.find(id='queryForm').get('action')
#print(api_url)

api_url=main_url+api_url
#print(api_url)


#crsf code

crsf_code=soup.find(id='queryForm').find('input').get('value')
#print(crsf_code)

#組成表單資料

FromData={
_csrf: c594e70b-f722-4dee-b332-e5ec15a2bd90
trainTypeList: ALL
transfer: ONE
startStation: 0900-基隆
endStation: 4340-新左營
rideDate: 2020/07/08
startOrEndTime: true
startTime: 00:00
endTime: 23:59
}

today=time.strftime('%Y/%m/%d')
#print(today)

today='2020/10/27'

sTime='00:00'
eTime='23:59'

begin_station=station['基隆']
end_station=station['新左營']

print(begin_station,end_station)

formData={
    
    '_csrf': crsf_code,
    'trainTypeList': 'ALL',
    'transfer': 'ONE',
    'startStation': begin_station,
    'endStation': end_station,
    'rideDate': today,
    'startOrEndTime': 'true',
    'startTime': sTime,
    'endTime': eTime    
}

#print(formData)


#傳送表單資料

resp=requests.post(api_url,formData)

#print(resp.text)

soup=BeautifulSoup(resp.text,'lxml')
#print(soup)

trs=soup.find('table').find('tbody').find_all('tr',class_='trip-column')
#print(trs)

for tr in trs:
    for td in tr.find_all('td'):
        print(td.text.strip(),end='\t')
    print()


#輸出數據

for tr in trs:
    for td in tr.find_all('td'):
        print(td.text.strip().replace('\n',''),end='\t')
    print()
































