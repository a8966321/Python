# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:42:41 2020

@author: Ezio Kevin
"""

import requests
from bs4 import BeautifulSoup

def getSoup(url):
    resp=requests.get(url)
    resp.encoding='utf-8'
    if resp.status_code !=200:
        return None
    soup = BeautifulSoup(resp.text,'lxml')
    return soup

url= input('請輸入網址 :')
soup=getSoup(url)
soup
