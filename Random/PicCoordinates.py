import cv2
import numpy as np

def onClick (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print ([x, y])

cv2.namedWindow ('pic')
cv2.setMouseCallback ('pic', onClick)

img = cv2.imread ('../Images/blue-chicory.jpg')

cv2.imshow ('pic', img)
cv2.waitKey (0)
