# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:45:23 2020

@author: Ezio Kevin
"""

import requests,tools,json

api_url = 'https://tw.global.nba.com/stats2/scores/daily.json'

date = '2020-01-30'

from_data = {
    'countryCode': 'TW',
'gameDate': date,
'locale': 'zh_TW',
'tz': '+8'
}

#print(from_data)

resp = requests.get(api_url,from_data)
resp.encoding = 'utf-8'
#print(resp)

if resp.status_code ==200:
    json_data = json.loads(resp.text)
    #print(json_data)

games = json_data['payload']['date']['games']

for game in games:
    #print(game)


home_team = game['homeTeam']
print(home_team['profile']['name'])
print(home_team['score']['q1Score'],home_team['score']['q2Score'],home_team['score']['q3Score'],home_team['score']['q4Score'],
     home_team['score']['score'])

away_team = game['awayTeam']
print(away_team['profile']['name'])
print(away_team['score']['q1Score'],away_team['score']['q2Score'],away_team['score']['q3Score'],away_team['score']['q4Score'],
      away_team['score']['score'])

for game in games:
    home_team = game['homeTeam']
    print('主隊:'+home_team['profile']['name'])
    print(home_team['score']['q1Score'],home_team['score']['q2Score'],home_team['score']['q3Score'],home_team['score']['q4Score'],
          home_team['score']['score'])

    away_team = game['awayTeam']
    print('客隊:'+away_team['profile']['name'])
    print(away_team['score']['q1Score'],away_team['score']['q2Score'],away_team['score']['q3Score'],away_team['score']['q4Score'],
          away_team['score']['score'])
    print('*'*30)

list_data = []

for game in games:
    home_team = game['homeTeam']
    away_team = game['awayTeam']
    
    list_data.append([date,home_team['profile']['name'],home_team['score']['q1Score'],home_team['score']['q2Score'],home_team['score']['q3Score'],home_team['score']['q4Score'],
          home_team['score']['score'],away_team['profile']['name'],away_team['score']['q1Score'],away_team['score']['q2Score'],away_team['score']['q3Score'],
                     away_team['score']['q4Score'],away_team['score']['score']])
    #print('主隊:'+home_team['profile']['name'])
    #print(home_team['score']['q1Score'],home_team['score']['q2Score'],home_team['score']['q3Score'],home_team['score']['q4Score'],
    #     home_team['score']['score'])

    
    #print('客隊:'+away_team['profile']['name'])
    #print(away_team['score']['q1Score'],away_team['score']['q2Score'],away_team['score']['q3Score'],away_team['score']['q4Score'],
    #     away_team['score']['score'])
print(list_data)



def getNBA(date):
    api_url = 'https://tw.global.nba.com/stats2/scores/daily.json'
    from_data = {
        'countryCode': 'TW',
        'gameDate': date,
        'locale': 'zh_TW',
        'tz': '+8'}
    
    resp = requests.get(api_url,from_data)
    games=json.loads(resp.text)
    datas = []
    if games['payload']['date']==None:
        return datas
    games_data = games['payload']['date']['games']
    for game in games_data:
        home_team = game['homeTeam']
        away_team = game['awayTeam']
    
        datas.append([date,home_team['profile']['name'],home_team['score']['q1Score'],home_team['score']['q2Score'],home_team['score']['q3Score'],home_team['score']['q4Score'],
          ])
        
        datas.append([date,away_team['profile']['name'],away_team['score']['q1Score'],away_team['score']['q2Score'],away_team['score']['q3Score'],
                     away_team['score']['q4Score']])
    
    return datas
    
#抓取指定日期
getNBA('2020-01-30')


#日期變換

import datetime

today=datetime.date.today()

print(today.strftime('%Y-%m-%d'))

today+datetime.timedelta(days=-1)

today+datetime.timedelta(days=1)

#將日期進行轉換成datetime物件
#進行自動累加天數及最後擷取日期

startDay=datetime.datetime(2019,1,1)

endDay=datetime.datetime(2019,1,31)

print(startDay,endDay)

while startDay<=endDay:    
    
    print(startDay.strftime("%Y-%m-%d"))
    startDay+=datetime.timedelta(days=1)
   
#連續抓取資料

import time
import requests,json

startDay=datetime.datetime(2019,1,1)
endDay=datetime.datetime(2019,12,31)


nbaData=[]


while startDay<=endDay: 
    day=startDay.strftime("%Y-%m-%d")
    print(f'擷取日期:{day}')
    tempData=getNBA(day)
    if tempData!=[]:
        nbaData+=tempData
    else:
        print(day+'當天無比賽')
        
    startDay+=datetime.timedelta(days=1)
    time.sleep(1)
    
    
print(nbaData)


#存成CSV
import pandas as pd

df1=pd.DataFrame(nbaData,columns=['日期','隊伍','round1','round2','round3','round4'])
df1.to_csv('NBA_2019_year.csv',encoding='utf-8-sig',index=0)


#print(df1)

































































