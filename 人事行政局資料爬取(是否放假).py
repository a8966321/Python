# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:50:44 2020

@author: Ezio Kevin
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

def getSoup(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    if resp.status_code !=200:
        return None
    soup = BeautifulSoup(resp.text,'lxml')
    return soup

url='https://rbdkd67zcc92ou2hpwdvxa-on.drv.tw/www/test_table1.html'
soup=getSoup(url)
#print(soup)


trs = soup.find(id='Table').find_all('tr')
#prnit(trs)


datas=[]
for i,tr in enumerate(trs[:-1]):
    data=[]
    print('-------------------------------------------------------------')
    if i==0:
        for th in tr.find_all('th'):
            print(th.text.strip(),end='|')
            data.append(th.text.strip())
    else:
        for td in tr.find_all('font'):
            print(td.text.strip(),end='|')
            data.append(td.text.strip())
    print()
    datas.append(data)

print(datas)

#存成csv檔
df1 = pd.DataFrame(datas)
df1.to_csv('人事行政局資料.csv',encoding='utf-8-sig',index=0)





