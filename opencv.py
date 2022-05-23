# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:02:44 2022

@author: Aorus
"""

import numpy as np
import cv2
import pyttsx3

# engine = pyttsx3.init()
# engine.setProperty('rate', 175)
# engine.say("Please select one option from below.  A) visually challenged.  B)hearing challenged")
# engine.runAndWait()
# rate = engine.getProperty('rate')
# print(rate)


while True:


    #blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
    
    img = cv2.imread('white.jpg')
    scale_percent = 170 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
      
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
     
     # Pay attention! 'cv2.imshow' takes images in BGR format
     
    
     
    text = "Data types are the classification or categorization of data items. It represents the kind of \n  value that tells what operations can be performed on a particular data. "
    y0, dy = 25, 50
    for i, line in enumerate(text.split('\n')):
          y = y0 + i*dy
          cv2.putText(resized, line, (25, y ), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,70,52),3)
     
    #cv2.putText(blank_image, " Please select one option from below : whether you are a visually chalenged or hearing challenged", (50,75), cv2.FONT_HERSHEY_SIMPLEX, 1 ,(230,70,52))
     
    
     
     
    cv2.imshow("Black Blank", resized)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()

