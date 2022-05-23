# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:17:36 2021

@author: rupen
"""

import numpy as np
import cv2

mylist= ['A','B','C','Rupendra','']
x = []

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Write some Text

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2

for n in mylist:
    x = ''.join(mylist)
    cv2.putText(img ,x,bottomLeftCornerOfText, font, fontScale,fontColor,)
    

print(x)
#Display the image
cv2.imshow("img",img)

#Save image
cv2.imwrite("out.jpg", img)

cv2.waitKey(0)
# Destroying opened window with name 'Detections'
cv2.destroyWindow('img')