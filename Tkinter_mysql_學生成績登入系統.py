# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 23:11:32 2019

@author: Jerry
"""

import tkinter as tk
import os,sqlite3
#import myTools as mt



def openDataBase(file_name,sql_table,overwrite=False):
    """建立資料庫"""
    if not os.path.exists(file_name) or overwrite:
        #刪除原本檔案並重新建立檔案
        if os.path.exists(file_name):
            os.remove(file_name)            
        conn=sqlite3.connect(file_name)
        try:
            cur=conn.cursor()
            #建立table
            cur.execute(sql_table)  
            conn.commit()  
               
        except Exception as e:
            print(e)
        else:
            print('write table success!')
            print('conn success!')
            return conn
      

    conn=sqlite3.connect(file_name) 
    print('conn success!')
    return conn



win=tk.Tk()
win.title('學生成績建檔系統')
frame1=tk.Frame(win)
frame1.pack(fill='x')
frame2=tk.Frame(win)
frame2.pack(fill='x')
frame3=tk.Frame(win,bg='yellow')
frame3.pack(fill='x')
frame4=tk.Frame(win)
frame4.pack(fill='x')       


def showMainMenu():
    
    label0=tk.Label(frame1,text='資料庫連結:',font=('Arial',12),bg='black',fg='white'
                    ,anchor='w')
    label0.pack(fill='x')    
    label=tk.Label(frame2,text='成績建檔系統',font=('Arial',40))
    label.grid(row=0,column=0,columnspan=2,padx=20,pady=5)
    label1=tk.Label(frame2,text='學號',font=('Arial',16))
    label1.grid(row=1,column=0)
    entry1=tk.Entry(frame2,bg='cyan',fg='black',font=('Arial',16),borderwidth=3)
    entry1.grid(row=1,column=1,pady=5)
    label2=tk.Label(frame2,text='姓名',font=('Arial',16))
    label2.grid(row=2,column=0)
    entry2=tk.Entry(frame2,bg='cyan',fg='black',font=('Arial',16),borderwidth=3)
    entry2.grid(row=2,column=1,pady=5)
    label3=tk.Label(frame2,text='國文',font=('Arial',16))
    label3.grid(row=3,column=0)
    entry3=tk.Entry(frame2,bg='cyan',fg='black',font=('Arial',16),borderwidth=3)
    entry3.grid(row=3,column=1,pady=5)
    label4=tk.Label(frame2,text='英文',font=('Arial',16))
    label4.grid(row=4,column=0)
    entry4=tk.Entry(frame2,bg='cyan',fg='black',font=('Arial',16),borderwidth=3)
    entry4.grid(row=4,column=1,pady=5)
    label5=tk.Label(frame2,text='數學',font=('Arial',16))
    label5.grid(row=5,column=0)
    entry5=tk.Entry(frame2,bg='cyan',fg='black',font=('Arial',16),borderwidth=3)
    entry5.grid(row=5,column=1,pady=5)    
    
    #提交
    def write():
        #是否有資料庫物件
        if cursor==None:              
            label0.config(text='資料庫未連結!',fg='red')
            return        
        
        #是否輸入為空        
        if entry1.get()=='' or entry2.get()=='':
            label0.config(text='輸入錯誤!',fg='red')
            return
        
        try:            
            #算平均分
            avg=round((int(entry3.get())+int(entry4.get())+int(entry5.get()))/3,2)                    
        except:                     
            label0.config(text='輸入錯誤',fg='yellow')
            return           
     
        #sql command
        sql_str="insert into info(學號,姓名,國文,數學,英文,average) values ('{}',\
        '{}',{},{},{},{});".format(entry1.get(),entry2.get(),entry3.get(),
        entry4.get(),entry5.get(),avg)
        #寫入資料庫
        cursor.execute(sql_str)
        #確認連結執行
        conn.commit()
        label0.config(text='寫入成功!',fg='yellow')    
        print('write sccuess!') 
        view()
        
    
    #開啟資料庫
    def open():    
        global conn
        global cursor
        conn=openDataBase(db_name,table_str,False)
        cursor=conn.cursor()
        print('open success!')
        label0.config(text='資料庫連結成功!',fg='yellow')        
    #檢視
    def view():
        if cursor==None:              
            label0.config(text='資料庫未連結!',fg='red')
            return
        
        #設定到list
        data_list=list(cursor.execute('select * from info'))       
        list_var.set(data_list)     
        
    #關閉資料庫
    def close():
        if conn!=None:
            conn.close()
        win.destroy()      
        
    #刪除資料
    def delete():       
        if cursor==None:              
            label0.config(text='資料庫未連結!',fg='red')
            return        
        
        #檢查listbox是否有選擇
        if listbox.curselection()!=():
            select_value=listbox.get(listbox.curselection())
            sql_str="delete from info where 學號='{}'".format(select_value[1])
        elif entry1.get()!="": #檢查學號輸入是否有值
            sql_str="delete from info where 學號='{}'".format(entry1.get())
        else: 
            sql_str='delete from info' #刪除全部
            
        cursor.execute(sql_str)
        conn.commit()
        label0.config(text='刪除成功!',fg='yellow')  
        view()
       
        
    
    button1=tk.Button(frame3,text='開啟',font=('Arial',15),command=open)
    button1.grid(row=0,column=0,padx=10,pady=10)
    button2=tk.Button(frame3,text='提交',font=('Arial',15),command=write)
    button2.grid(row=0,column=1,padx=10,pady=10)
    button3=tk.Button(frame3,text='檢視',font=('Arial',15),command=view)
    button3.grid(row=0,column=2,padx=10,pady=10)
    button4=tk.Button(frame3,text='刪除',font=('Arial',15),command=delete)    
    button4.grid(row=0,column=3,padx=10,pady=10)   
    button5=tk.Button(frame3,text='結束',font=('Arial',15),command=close)
    button5.grid(row=0,column=4,padx=10,pady=10)
       
    
    listbox=tk.Listbox(frame4,listvariable=list_var,font=('Arial',12),bg='dark red',fg='white')
    listbox.pack(fill='x')

table_str='''CREATE TABLE "info" (
    	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        "學號"	TEXT NOT NULL,
    	"姓名"	TEXT NOT NULL,
    	"國文"	REAL,
    	"數學"	REAL,
    	"英文"	REAL,
        "average" REAL
);'''

conn=None
cursor=None
db_name='student.db'
list_var=tk.StringVar()
list_var.set([123,456])


showMainMenu()
win.mainloop()
