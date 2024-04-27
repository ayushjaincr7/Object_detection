import cv2
import time
import numpy as np
import sys
import os
sys.path.append('/Users/ayushjain/Documents/object_detection/Hand_tracking/')
import math
# Import the module
import HandTrackingModule as htm



wCam, hCam= 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "FingerImage"
myList = os.listdir(folderPath)
# print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)


print(len(overlayList))

while True:
    success, img = cap.read()

    img[0:200, 0:200] = overlayList[1].resize((200, 200))
    cv2.imshow('Image',img)

    cv2.waitKey(1)

