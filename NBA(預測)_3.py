# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:01:46 2020

@author: Ezio Kevin
"""

import pandas as pd

df1=pd.read_csv('nba_data.csv',encoding='utf-8-sig')

#print(df1.head())

df1.drop('隊伍',axis=1,inplace=True)

#print(df1.head(6))

datas=df1.values.tolist()

#print(len(datas))

nba_data=[]
for i in range(len(datas)):  
    if i%2==0:
        #print(datas[i][0],datas[i][1]+datas[i+1][1],datas[i][2]+datas[i+1][2],datas[i][3]+datas[i+1][3],datas[i][4]+datas[i+1][4])
        nba_data.append([datas[i][0],datas[i][1]+datas[i+1][1],datas[i][2]+datas[i+1][2],datas[i][3]+datas[i+1][3],datas[i][4]+datas[i+1][4]])

#print(nba_data)


def get_day_data(numbers):    
    count=0
    win_count=0
    while count<len(numbers):            
        #奇數
        if numbers[count]%2!=0:
            win_count+=1           
            #假如已經兩勝!
            if win_count==2:
                break
        else:            
            win_count-=1
            #輸一或歸零就離開
            if win_count<=0:
                break
        count+=1       
        
    return win_count

total_win_count=0

print(get_day_data(nba_data[9][1:]))


#win_count


#瘋狂投注版本


count=0
total_win_count=0
total_win_list=[]
for data in nba_data:
    total_win_count+=get_day_data(data[1:])
    total_win_list.append(total_win_count)
    count+=1
    
print('共%d場'%count)
print(total_win_count)

import pandas as pd
import matplotlib.pyplot as plt

s1=pd.Series(total_win_list)

s1.plot()

plt.show()


#一天只投注一次


count=0
total_win_count=0
total_win_list=[]
day=""
for data in nba_data:
    if day!=data[0]:
        day=data[0]
        total_win_count+=get_day_data(data[1:])
        total_win_list.append(total_win_count)
        count+=1
    
print('共%d場'%count)
print(total_win_count)



import pandas as pd
import matplotlib.pyplot as plt

s1=pd.Series(total_win_list)
s1.plot()

plt.show()



#只投注某局


def get_day_data_round(numbers,count):        
    win_count=0
    #奇數
    if numbers[count]%2==0:
        win_count=1              
    else:            
        win_count=-1     
        
    return win_count

count=0
total_win_count=0
temp_win_count=0
total_win_list=[]
#第一天開始
day=nba_data[0][0]

change_day=False

for data in nba_data:        
    
    #換天
    if change_day:
        if day==data[0]:
            continue
        day=data[0]         
        change_day=False
         
    
    #沒有換天
    if not change_day:             
        #同一天
        if day==data[0]:     
            count+=1
            win_count=get_day_data_round(data[1:],2)

            #平手換天
            if temp_win_count==1 and win_count==-1:
                temp_win_count+=win_count
                change_day=True
            #輸一
            elif win_count==-1:
                temp_win_count=-1
                change_day=True
            #贏分
            elif win_count==1:
                temp_win_count+=win_count
                if temp_win_count==2:
                    change_day=True  
        else:
            change_day=True
            
        if change_day:
            total_win_count+=temp_win_count
            total_win_list.append(total_win_count)
            temp_win_count=0
        
           
            
            
    
    
print('共%d場'%count)
print(total_win_count)




import pandas as pd
import matplotlib.pyplot as plt

s1=pd.Series(total_win_list)
s1.plot()

plt.show()



































































































