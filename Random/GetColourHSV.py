# Returns the value of a particular pixel in HSV

import cv2
import numpy as np

def getColour (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        BGR = np.uint8([[frame [y, x]]])
        HSV = cv2.cvtColor (BGR, cv2.COLOR_BGR2HSV)
        print (HSV)

webcam = cv2.VideoCapture (0)
cv2.namedWindow ('webcam')
cv2.setMouseCallback ('webcam', getColour)

while True:
    x, frame = webcam.read ()

    cv2.imshow ('webcam', frame)

    if cv2.waitKey (1) & 0xFF == 27:
        break
