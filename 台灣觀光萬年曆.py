# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:14:32 2020

@author: Ezio Kevin
"""

import requests
from bs4 import BeautifulSoup

api_url = 'https://www.taiwan.net.tw/m1.aspx?sNo=0001019&keyString=^^^^20200701^20201231'
url = 'https://www.taiwan.net.tw/m1.aspx'
form_Data = {
    'sNo': '0001019',
    'keyString': '^^^^20200101^20201231',
    'page':1
    
}

resp = requests.get(url , form_Data)
#print(resp)

if resp.status_code==200:
    soup=BeautifulSoup(resp.text,'lxml')
#print(soup)


#爬取網頁所需資料
#並整理
if resp.status_code==200:
    soup=BeautifulSoup(resp.text,'lxml')
    #print(soup)
    
    lis=soup.find('ul',class_='columnBlock-list').find_all('li')
    
    print(len(lis))
    
    for li in lis:
        print(li.find('a')['href'])
        print(li.text.strip())














