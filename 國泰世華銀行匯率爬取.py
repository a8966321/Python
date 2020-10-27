# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:47:18 2020

@author: Ezio Kevin
"""

import requests
from bs4 import BeautifulSoup

url='https://www.cathaybk.com.tw/cathaybk/personal/deposit-exchange/rate/currency-billboard/'
resp=requests.get(url)
resp.encoding = 'utf-8'
soup=BeautifulSoup(resp.text,'lxml')
#print(soup)


table = soup.find('table',class_="table-rate text-left")
#print(table)


ths=table.find('thead')
ths=[th.text.strip() for th in ths.find_all('th')]
ths=[th.replace('\n',' ') for th in ths]
#print(ths)


trs=table.find('tbody').find_all('tr')
datas=[]

for tr in trs:
    tds=[td.text.strip() for td in tr.find_all('td')]
    datas.append(tds)

#print(datas)


import csv

if datas!=[]:
    with open('國泰世華銀行匯率.csv','w',newline='',encoding='utf-8-sig') as f:
        writer=csv.writer(f)
        writer.writerow(ths)
        writer.writerows(datas)
    print('檔案輸出完畢')










