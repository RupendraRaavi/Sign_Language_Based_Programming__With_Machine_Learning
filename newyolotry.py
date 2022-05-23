# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:35:58 2021

@author: rupen
"""


#rom ..convenience import is_cv3
import cv2

vid = cv2.VideoCapture(0)

while (True):
    
    ret,frame = vid.read()
    
    cv2.imshow('frame',frame)
    
    length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    print( length )
    
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
    
vid.release()

cv2.destroyAllWindows()