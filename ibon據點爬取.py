# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:57:18 2020

@author: Ezio Kevin
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


def getSoup(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    if resp.status_code !=200:
        return None
    soup = BeautifulSoup(resp.text,'lxml')
    return soup


url='http://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0'
soup=getSoup(url)
#print(soup)

api_url = 'http://www.ibon.com.tw/retail_inquiry_ajax.aspx'

formData = {
    'strTargetField': 'COUNTY',
    'strKeyWords': '台北市'
}

resp = requests.post(api_url,formData)
#print(resp)

#print(resp.text)


soup = BeautifulSoup(resp.text,'lxml')
datas = soup.text.strip().split()
#print(datas)


trs = soup.find('table').find_all('tr')
datas = []
for tr in trs:
    data = []
    for td in tr.find_all('td'):
        #print(td.text,end='\t')
        data.append(td.text.strip())
    #print()
    datas.append(data)
#print(datas)
    
    
url='http://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0'
soup=getSoup(url)
#print(soup)
    
ps=soup.find('div',class_='searchmap').find_all('p')
#print(ps)    

#找出所有城市

citys =[p.text.strip() for p in ps ]
#print(citys)

def getIbonData(city):  
    datas=[]
    formData={
        'strTargetField': 'COUNTY',
        'strKeyWords':city
    }
    
    resp=requests.post(api_url,data=formData)    
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'lxml')   
        trs=soup.find('table').find_all('tr')        
        for tr in trs: 
            tds=tr.find_all('td')
            datas.append([td.text.strip() for td in tds])       
    else:
        print(city+"抓取錯誤!")
    
    
    return datas
    
ibon={}   

#抓取各縣市資料

for city in citys:
    print(city+" 資料擷取中.....")
    ibon[city]=getIbonData(city)
    
#print(ibon)
    
    
#test

#print(ibon['台北市'])
    
    
{city:getIbonData(city) for city in citys}    
    
#儲存成xls檔案格式    



writer = pd.ExcelWriter('ibon站地點.xls', engine = 'xlsxwriter')

for city in citys:
    df = pd.DataFrame.from_dict(ibon[city][1:])
    df.columns=ibon[city][0]
    df.index=df['店號']
    df=df.drop('店號',axis=1)
    
    df.to_excel(writer,sheet_name=city)
    
writer.save()
writer.close()
    
    
    
    
    
    
    
    



