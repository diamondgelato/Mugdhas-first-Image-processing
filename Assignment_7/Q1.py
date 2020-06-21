'''
'''

import cv2
import numpy as np

def nothing (x):
    pass

webcam = cv2.VideoCapture (0)
cv2.namedWindow ('webcam')

# making the trackbars

cv2.createTrackbar ('lower hue', 'webcam', 0, 179, nothing)
cv2.createTrackbar ('lower saturation', 'webcam', 0, 255, nothing)
cv2.createTrackbar ('lower vibrance', 'webcam', 0, 255, nothing)
cv2.createTrackbar ('higher hue', 'webcam', 0, 179, nothing)
cv2.createTrackbar ('higher saturation', 'webcam', 0, 255, nothing)
cv2.createTrackbar ('higher vibrance', 'webcam', 0, 255, nothing)

while True:
    x, frame = webcam.read ()
    HSVFrame = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

    # getting trackbar positions

    lowerHSV = np.array ([cv2.getTrackbarPos ('lower hue', 'webcam'),
                          cv2.getTrackbarPos ('lower saturation', 'webcam'),
                          cv2.getTrackbarPos ('lower vibrance', 'webcam')])

    higherHSV = np.array ([cv2.getTrackbarPos ('higher hue', 'webcam'),
                           cv2.getTrackbarPos ('higher saturation', 'webcam'),
                           cv2.getTrackbarPos ('higher vibrance', 'webcam')])

    # print (str(lowerHSV) + ' ' + str(higherHSV))

    # colour filtering

    mask = cv2.inRange (HSVFrame, lowerHSV, higherHSV)
    result = cv2.bitwise_and (frame, frame, mask = mask)

    # display flitered image

    cv2.imshow ('webcam', result)
    if cv2.waitKey(1) & 0xFF == 27:                     # press 'esc' to exit
        break
