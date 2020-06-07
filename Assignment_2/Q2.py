# Obtain a dataset of an object from live webcam feed. The Output Image Data set should be named in the following format:
# 	IMG_1.jpg, IMG_2.jpg and so on.

import cv2

webcam = cv2.VideoCapture (0)
counter = 1
pathFormat = '../WebcamImages/IMG_{0}.jpg'

while counter <= 100:
    x, frame = webcam.read()

    path = pathFormat.format (counter)

    cv2.imwrite (path, frame)
    counter += 1
