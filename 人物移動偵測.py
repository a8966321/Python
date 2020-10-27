# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:00:35 2020

@author: Ezio Kevin
"""

import cv2
cap = cv2.VideoCapture('vtest.avi')
bg=None

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (17,17), 0)
    
    if bg is None:
        bg = gray
        continue
    
    diff = cv2.absdiff(gray, bg) #影像相減
    diff = cv2.threshold(diff,30,255,cv2.THRESH_BINARY)[1] #二值化處理 
    diff = cv2.erode(diff,None,iterations = 2) #侵蝕處理
    diff = cv2.dilate(diff, None ,iterations = 2) #膨脹處理
    
    cnts , hierarchy = cv2.findContours(
        diff, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        if cv2.contourArea(c) <500:
            continue
        
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        
        
    cv2.imshow('frame', frame)
    if cv2.waitKey(100) ==27:
        cv2.destroyAllWindows()
        break