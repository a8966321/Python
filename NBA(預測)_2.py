# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:49:49 2020

@author: Ezio Kevin
"""
import json
import requests
from bs4 import BeautifulSoup

def getSoup(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    if resp.status_code!=200:
        return None
    return BeautifulSoup(resp.text,'lxml')   

url='https://tw.global.nba.com/scores/#!/2020-01-31'

soup=getSoup(url)
#print(soup)

trs=soup.find('div',class_='final-game-table-wrapper').find('table').find_all('tr')
#print(trs)

for tr in trs:
    tds=[td for td in tr.find_all('td')]
    for td in tds:
        print(td.text.strip(),end='\t')
        
    print()

#觀察api

url='https://tw.global.nba.com/scores/'

apiUrl='https://tw.global.nba.com/stats2/scores/daily.json'

formData={    
    'countryCode': 'TW',
    'gameDate': '2020-01-31',
    'locale': 'zh_TW',
    'tz': '+8',
}



resp=requests.get(apiUrl,formData)

#print(resp)




#使用json套件分析
json_data=json.loads(resp.text)
#print(json_data)


#找出比分區段

game_data=json_data['payload']['date']['games']

#print(game_data)


#開始查找球隊分數資料

home_team=game_data[0]['homeTeam']

print(home_team['profile']['name'])
print(home_team['score']['q1Score'],home_team['score']['q2Score'],home_team['score']['q3Score'],home_team['score']['q4Score'],
     home_team['score']['score'])

print()
away_team=game_data[0]['awayTeam']

print(away_team['profile']['name'])
print(away_team['score']['q1Score'],away_team['score']['q2Score'],away_team['score']['q3Score'],away_team['score']['q4Score'],
     away_team['score']['score'])

#當天全部資料

for game in game_data:
    
    print('*'*50)
    home_team=game['homeTeam']
    print(home_team['profile']['name'])
    print(home_team['score']['q1Score'],home_team['score']['q2Score']
    ,home_team['score']['q3Score'],home_team['score']['q4Score'],
         home_team['score']['score'])
    
    
    away_team=game['awayTeam']
    
    print(away_team['profile']['name'])
    print(away_team['score']['q1Score'],away_team['score']['q2Score']
    ,away_team['score']['q3Score'],away_team['score']['q4Score'],
         away_team['score']['score'])
    

print('*'*50)


#宣告成函式
def getNBAData(date):
       
    apiUrl='https://tw.global.nba.com/stats2/scores/daily.json'
    formData={    
        'countryCode': 'TW',
        'gameDate': date,
        'locale': 'zh_TW',
        'tz': '+8',
    }
    
    resp=requests.get(apiUrl,formData)
    games=json.loads(resp.text)
    
      
    datas=[]    
    
    if games['payload']['date']==None:
        return datas
           
    game_data=games['payload']['date']['games']

    for game in game_data:

        homeTeam=game['homeTeam']
        awayTeam=game['awayTeam']

        #print('*'*50)

        datas.append([date,homeTeam['profile']['name'],
                     homeTeam['score']['q1Score'],homeTeam['score']['q2Score'],
             homeTeam['score']['q3Score'],homeTeam['score']['q4Score']])

        datas.append([date,awayTeam['profile']['name'],
                     awayTeam['score']['q1Score'],awayTeam['score']['q2Score'],
             awayTeam['score']['q3Score'],awayTeam['score']['q4Score']])           
            

    return datas


print(getNBAData('2020-01-31'))

#處理沒有比賽得日期

#print(getNBAData('2020-07-1'))


#連續日期抓取

import datetime

today=datetime.date.today()

print(today.strftime('%Y-%m-%d'))

print(today+datetime.timedelta(days=-1))

print(today+datetime.timedelta(days=1))

#將日期進行轉換成datetime物件
#進行自動累加天數及最後擷取日期

startDay=datetime.datetime(2019,1,1)

endDay=datetime.datetime(2019,1,31)

print(startDay,endDay)



#自動累加日期

while startDay<=endDay:    
    
    print(startDay.strftime("%Y-%m-%d"))
    startDay+=datetime.timedelta(days=1)


#連續抓取資料

import time
import requests,json

startDay=datetime.datetime(2019,1,1)
endDay=datetime.datetime(2019,1,5)


nbaData=[]


while startDay<=endDay: 
    day=startDay.strftime("%Y-%m-%d")
    print(f'擷取日期:{day}')
    tempData=getNBAData(day)
    if tempData!=[]:
        nbaData+=tempData
    else:
        print(day+'當天無比賽')
        
    startDay+=datetime.timedelta(days=1)
    time.sleep(1)
    
    
print(nbaData)   

#儲存csv

import pandas as pd

df1=pd.DataFrame(nbaData,columns=['日期','隊伍','round1','round2','round3','round4'])
df1.to_csv('NBA_DATA.csv',encoding='utf-8-sig',index=0)


#局數分析

#分析每round分數總和的奇數跟偶數比例

#print(df1)
#print(df1['round3'])

s1=df1['round3']

for i in range(len(s1)):
    print(s1[i])

#print(len(s1))

#合併分數

count=0
score=0
scores=[]

for i in range(len(s1)):
    count+=1
    score+=s1[i]
    
    if count%2==0:      
        scores.append(score)
        score=0
       
print(len(scores))


#開偶數場數

s2=pd.Series(scores)
#print(s2)

len(s2[s2%2==0])

print('{:.2%}'.format(len(s2[s2%2==0])/len(s2)))

#函式化

def getWinAverage(data):
    count=0
    score=0
    scores=[]
  

    for i in range(len(data)):
        count+=1
        score+=data[i]

        if count%2==0:      
            scores.append(score)
            score=0
            
    s2=pd.Series(scores)
   
            
    return round(len(s2[s2%2==0])/len(s2)*100,2),round(len(s2[s2%2!=0])/len(s2)*100,2)
            
#print(getWinAverage(df1['round3']))


#總局數查詢


for r in ['round1','round2','round3','round4']:
    print(r)
    print('偶數勝率 vs 奇術勝率')
    print(getWinAverage(df1[r]))

#函式化
#抓取週期跟勝率分析進行整合


import datetime 
datetime.date.fromisoformat('2019-12-04')

#print(datetime.datetime(2019,1,1))


import time
import requests,json
import datetime 
import pandas as pd

def getAllNbaData(start,end):
        
    startDay=datetime.date.fromisoformat(start)
    endDay=datetime.date.fromisoformat(end)    
    nbaData=[]

    while startDay<=endDay: 
        day=startDay.strftime("%Y-%m-%d")
        print(f'擷取日期:{day}')
        tempData=getNBAData(day)
        if tempData!=[]:
            nbaData+=tempData
        else:
            print(day+'當天無比賽')

        startDay+=datetime.timedelta(days=1)
        time.sleep(1)
        
        
        
    df1=pd.DataFrame(nbaData,columns=['日期','隊伍','round1','round2','round3','round4'])
    for r in ['round1','round2','round3','round4']:
        print(r)
        print('偶數勝率 vs 奇術勝率')
        print(getWinAverage(df1[r]))
        
    
    print("============================================================================")
    return nbaData   

#print(getAllNbaData('2019-01-01','2019-01-31'))
    


#2012~2019 勝率分析

import pandas as pd
import datetime
import matplotlib.pyplot as plt

today=datetime.datetime.today()

file_name='nba_all_data.csv'


df1=pd.read_csv(file_name,encoding='utf-8-sig')

round_str=['round1','round2','round3','round4']

date=''
for r in round_str:       
    s1=df1[r]
    scores=[]
    score=0
    #加總每局的總分
    count=0
    for s in s1:
         count+=1
         score+=s
         if count%2==0:
            scores.append(score)
            score=0

    s1=pd.Series(scores)
    
    #print(s1)
    #print(r)
    print("總場數:%d"%len(s1))
    print("該局總和分數奇數:{} 機率:{:.2%}".format(len(s1[s1%2!=0]),len(s1[s1%2!=0])/len(s1)))
    print("該局總和分數偶數:{} 機率:{:.2%}".format(len(s1[s1%2==0]),len(s1[s1%2==0])/len(s1)))
    #break
    #s1.plot()
    #plt.show()








































































