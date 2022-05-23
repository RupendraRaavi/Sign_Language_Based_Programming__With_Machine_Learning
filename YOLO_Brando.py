# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:01:11 2022

@author: Aorus
"""


"""
Author : Rupendra
"""


# Detecting Objects in Real Time with OpenCV deep learning library
#
# Algorithm:
# Reading stream video from camera --> Loading YOLO v3 Network -->
# --> Reading frames in the loop --> Getting blob from the frame -->
# --> Implementing Forward Pass --> Getting Bounding Boxes -->
# --> Non-maximum Suppression --> Drawing Bounding Boxes with Labels -->
# --> Showing processed frames in OpenCV Window
#
# Result:
# Window with Detected Objects, Bounding Boxes and Labels in Real Time


# Importing needed libraries
import PySimpleGUI as pg
import numpy as np
import cv2
import time
import tensorflow as tf
import pyttsx3
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
"""
Start of:
Reading stream video from camera
"""

# Defining 'VideoCapture' object
# and reading stream video from camera
camera = cv2.VideoCapture(0)

# Preparing variables for spatial dimensions of the frames
h, w = None, None

"""
End of:
Reading stream video from camera
"""


"""
Start of:
Loading YOLO v3 network
"""

# Loading COCO class labels from file
# Opening file
# Pay attention! If you're using Windows, yours path might looks like:
# r'yolo-coco-data\coco.names'
# or:
# 'yolo-coco-data\\coco.names'
with open('yolo-coco-data/obj.names') as f:
    # Getting labels reading every line
    # and putting them into the list
    labels = [line.strip() for line in f]


# # Check point
# print('List with labels names:')
#print(labels)

# Loading trained YOLO v3 Objects Detector
# with the help of 'dnn' library from OpenCV
# Pay attention! If you're using Windows, yours paths might look like:
# r'yolo-coco-data\yolov3.cfg'
# r'yolo-coco-data\yolov3.weights'
# or:
# 'yolo-coco-data\\yolov3.cfg'
# 'yolo-coco-data\\yolov3.weights'
network = cv2.dnn.readNetFromDarknet('yolo-coco-data/yolov3-tiny-obj.cfg',
                                     'yolo-coco-data/yolov3-tiny-obj_50500.weights')

# Getting list with names of all layers from YOLO v3 network
layers_names_all = network.getLayerNames()

# # Check point
# print()
# print(layers_names_all)

# Getting only output layers' names that we need from YOLO v3 algorithm
# with function that returns indexes of layers with unconnected outputs
layers_names_output = \
    [layers_names_all[i - 1] for i in network.getUnconnectedOutLayers()]

# # Check point
# print()
# print(layers_names_output)  # ['yolo_82', 'yolo_94', 'yolo_106']

# Setting minimum probability to eliminate weak predictions
probability_minimum = 0.5

# Setting threshold for filtering weak bounding boxes
# with non-maximum suppression
threshold = 0.3

# Generating colours for representing every detected object
# with function randint(low, high=None, size=None, dtype='l')
colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

# # Check point
# print()
# print(type(colours))  # <class 'numpy.ndarray'>
# print(colours.shape)  # (80, 3)
# print(colours[0])  # [172  10 127]

"""
End of:
Loading YOLO v3 network
"""
detected = ''
#x = []

# engine = pyttsx3.init()
# engine.setProperty('rate', 175)
# engine.say("Please select one option from below. A)Python Variables  B)Python Data Types ")
# engine.runAndWait()
# rate = engine.getProperty('rate')
# print(rate)

def alphabet_c():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say("You have selected option A. Python Variable")
    engine.runAndWait()
    rate = engine.getProperty('rate')
    
    while True:
        img1= cv2.imread('white.jpg')
        scale_percent = 170 # percent of original size
        width = int(img1.shape[1] * scale_percent / 100)
        height = int(img1.shape[0] * scale_percent / 100)
        dim = (width, height)
          
        # resize image
        resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
        text = "A Python variable is a reserved memory location to store values. In other words, a variable \n in a python program gives data to the computer for processing. Every value in Python \n has a datatype. Different data types in Python are Numbers, List, Tuple, Strings, Dictionary \n etc."
        y0, dy = 25, 50
        for i, line in enumerate(text.split('\n')):
              y = y0 + i*dy
              cv2.putText(resized, line, (25, y ), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,70,52),3)
        cv2.imshow('Amercian sign language',resized)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()

    
def alphabet_b():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say("You have selected option B. Python Data Types")
    engine.runAndWait()
    rate = engine.getProperty('rate')
    
    while True:
        img2= cv2.imread('white.jpg')
        scale_percent = 170 # percent of original size
        width = int(img2.shape[1] * scale_percent / 100)
        height = int(img2.shape[0] * scale_percent / 100)
        dim = (width, height)
          
        # resize image
        resized = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)
        text = "Data types are the classification or categorization of data items. It represents the kind of \n  value that tells what operations can be performed on a particular data."
        y0, dy = 25, 50
        for i, line in enumerate(text.split('\n')):
              y = y0 + i*dy
              cv2.putText(resized, line, (25, y ), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,70,52),3)
              
        cv2.imshow('Amercian sign language',resized)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()
    

    
    

"""
Start of:
Reading frames in the loop
"""

# Defining loop for catching frames
while True:
    # Capturing frame-by-frame from camera
    _, frame = camera.read()

    # Getting spatial dimensions of the frame
    # we do it only once from the very beginning
    # all other frames have the same dimension
    if w is None or h is None:
        # Slicing from tuple only first two elements
        h, w = frame.shape[:2]

    """
    Start of:
    Getting blob from current frame
    """

    # Getting blob from current frame
    # The 'cv2.dnn.blobFromImage' function returns 4-dimensional blob from current
    # frame after mean subtraction, normalizing, and RB channels swapping
    # Resulted shape has number of frames, number of channels, width and height
    # E.G.:
    # blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size, mean, swapRB=True)
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)

    """
    End of:
    Getting blob from current frame
    """

    """
    Start of:
    Implementing Forward pass
    """

    # Implementing forward pass with our blob and only through output layers
    # Calculating at the same time, needed time for forward pass
    network.setInput(blob)  # setting blob as input to the network
    start = time.time()
    output_from_network = network.forward(layers_names_output)
    end = time.time()

    # Showing spent time for single current frame
    #print('Current frame took {:.5f} seconds'.format(end - start))

    """
    End of:
    Implementing Forward pass
    """

    """
    Start of:
    Getting bounding boxes
    """

    # Preparing lists for detected bounding boxes,
    # obtained confidences and class's number
    bounding_boxes = []
    confidences = []
    class_numbers = []

    # Going through all output layers after feed forward pass
    for result in output_from_network:
        # Going through all detections from current output layer
        for detected_objects in result:
            # Getting 80 classes' probabilities for current detected object
            scores = detected_objects[5:]
            # Getting index of the class with the maximum value of probability
            class_current = np.argmax(scores)
            # Getting value of probability for defined class
            confidence_current = scores[class_current]

            # # Check point
            # # Every 'detected_objects' numpy array has first 4 numbers with
            # # bounding box coordinates and rest 80 with probabilities
            # # for every class
            # print(detected_objects.shape)  # (85,)

            # Eliminating weak predictions with minimum probability
            if confidence_current > probability_minimum:
                # Scaling bounding box coordinates to the initial frame size
                # YOLO data format keeps coordinates for center of bounding box
                # and its current width and height
                # That is why we can just multiply them elementwise
                # to the width and height
                # of the original frame and in this way get coordinates for center
                # of bounding box, its width and height for original frame
                box_current = detected_objects[0:4] * np.array([w, h, w, h])

                # Now, from YOLO data format, we can get top left corner coordinates
                # that are x_min and y_min
                x_center, y_center, box_width, box_height = box_current
                x_min = int(x_center - (box_width / 2))
                y_min = int(y_center - (box_height / 2))

                # Adding results into prepared lists
                bounding_boxes.append([x_min, y_min,
                                       int(box_width), int(box_height)])
                confidences.append(float(confidence_current))
                class_numbers.append(class_current)

    """
    End of:
    Getting bounding boxes
    """

    """
    Start of:
    Non-maximum suppression
    """

    # Implementing non-maximum suppression of given bounding boxes
    # With this technique we exclude some of bounding boxes if their
    # corresponding confidences are low or there is another
    # bounding box for this region with higher confidence

    # It is needed to make sure that data type of the boxes is 'int'
    # and data type of the confidences is 'float'
    # https://github.com/opencv/opencv/issues/12789
    results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                               probability_minimum, threshold)

    """
    End of:
    Non-maximum suppression
    """

    """
    Start of:
    Drawing bounding boxes and labels
    """

    # Checking if there is at least one detected object
    # after non-maximum suppression
    if len(results) > 0:
        # Going through indexes of results
        for i in results.flatten():
            # Getting current bounding box coordinates,
            # its width and height
            x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
            box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]

            # Preparing colour for current bounding box
            # and converting from numpy array to list
            colour_box_current = colours[class_numbers[i]].tolist()

            # # # Check point
            # print(type(colour_box_current))  # <class 'list'>
            # print(colour_box_current)  # [172 , 10, 127]

            # Drawing bounding box on the original current frame
            cv2.rectangle(frame, (x_min, y_min),
                          (x_min + box_width, y_min + box_height),
                          colour_box_current, 2)

            # Preparing text with label and confidence for current bounding box
            text_box_current = '{}: {:.4f}'.format(labels[int(class_numbers[i])],
                                                   confidences[i])
            newtextbox = '{} '.format(labels[int (class_numbers[i])])
            
            k = cv2.waitKey(125)
            if k == ord('p'):
               if newtextbox == 'Space ':
                   newtextbox = newtextbox.replace('Space ', ' ')
                   detected = detected + newtextbox
               else:
                   newtextbox = newtextbox.replace(' ','')
                   detected = detected + newtextbox
                   
                
                
            
            
            
            
                
          
                
                
   
                
                 
                
                   
                
                
                
                
                
                
                #detected = detected + newtextbox  
                   #detected = detected.replace(' ','')
                   #print(detected)q
                   #detected = detected.replace('Space',' ')
               
                
              
            
                   
                     
           
                    
           
            
              
               # Setting up a sentence here
            
            
             # Putting text with label and confidence on the original image
             
            cv2.putText(frame, text_box_current, (x_min, y_min - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, colour_box_current, 2)
            
            
            
            
            

    """
    End of:
    Drawing bounding boxes and labels
    """

                   
    """
    Start of:
    Showing processed frames in OpenCV Window
    """

    # Showing results obtained from camera in Real Time

    # Showing current frame with detected objects
    # Giving name to the window with current frame
    # And specifying that window is resizable
    
    cv2.namedWindow('YOLO v3 Real Time Detections', cv2.WINDOW_NORMAL)
    blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
    
    # Pay attention! 'cv2.imshow' takes images in BGR format
    
    #cv2.putText (frame, 'Sentence : ' + str(detected) , (50,75),cv2.FONT_HERSHEY_SIMPLEX,1,(230,70,52),2,cv2.LINE_AA)
    
    
    
    # cv2.putText(blank_image, " Please select one option from below : whether you are a visually chalenged or hearing challenged", (50,75), cv2.FONT_HERSHEY_SIMPLEX, 1 ,(230,70,52))
    
    image = cv2.imread('ASL.jpeg')
    img = cv2.imread('Deaf_Blind_New.png')
    scale_percent = 170 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
      
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    text = "Please select one option from below \n \n  A) Python variables.  \n \n \n  B) Data Types"
    y0, dy = 25, 50
    for i, line in enumerate(text.split('\n')):
          y = y0 + i*dy
          cv2.putText(resized, line, (25, y ), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,70,52),3)
    
    
    cv2.imshow('Amercian sign language',image)
    cv2.imshow('YOLO v3 Real Time Detections', frame)
    # cv2.imshow("Black Blank", resized)
    
    
    
    
   
    
    
    
    #### This is GUI
   
    
    

    #Event loop



    
    
    
    
        
        

    # Breaking the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    
    """
    End of:
    Showing processed frames in OpenCV Window
    """

"""
End of:
Reading frames in the loop
"""


# Releasing camera
camera.release()
# Destroying all opened OpenCV windows
cv2.destroyAllWindows()


"""
Some comments

cv2.VideoCapture(0)

To capture video, it is needed to create VideoCapture object.
Its argument can be camera's index or name of video file.
Camera index is usually 0 for built-in one.
Try to select other cameras by passing 1, 2, 3, etc.
"""
# import PySimpleGUI as pg


# # Theme

# pg.theme('default1')


# # Layout

# layout = [
    
#     [
    
#     pg.Text("Enter name: "),
#     pg.InputText()
    
#     ],  
    
#     [
    
#     pg.Text("Enter age: "),
#     pg.InputText()
    
#     ], 
    
#     [
    
#     pg.Text("Select one option "),
#     pg.Radio("Visually Impaired", "group1"),
#     pg.Radio("Hearing Impaired", "group1")
    
#     ],
    
#     [
     
#      pg.Button("Ok"),
#      pg.Button("Close")
     
     
#      ]
# ]


# #Window

# window = pg.Window("Form",layout)

# #Event loop


# event, values = window.read()
# print(event)
# print(values)
    
    
