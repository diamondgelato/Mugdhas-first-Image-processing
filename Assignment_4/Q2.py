# Q2: Get a cropped frame using two mouse clicks

import cv2
import numpy as np

points = np.zeros(shape = (2, 2), dtype = int)
index = 0
img = cv2.imread ('../Images/blue-chicory.jpg')

def onClick (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global index
        global points

        if (index < 2):
            points[index] = [x, y]
            index = index + 1

            if np.all (points):
                cropImage ()
        else:
            pass

def cropImage ():
    global points
    pt0 = points [0]
    pt1 = points [1]

    if points [0][0] > points [1][0]:                                                               # 1st is to right of 2nd
        if points [0][1] > points [1][1]:                                                           # 1st is below 2nd
            cropped = img [ int(pt1[1]):int(pt0[1]), int(pt1[0]):int(pt0[0]) ]                      # 2nd is top-left and 1st is bottom-right
        elif points [0][1] < points [1][1]:                                                         # 1st is above 2nd
            cropped = img [ int(pt0[1]):int(pt1[1]), int(pt1[0]):int(pt0[0]) ]                      # 2nd is bottom-left and 1st is top-right
    elif points [0][0] < points [1][0]:                                                             # 1st is to left of 2nd
        if points [0][1] > points [1][1]:                                                           # 1st is below 2nd
            cropped = img [ int(pt1[1]):int(pt0[1]), int(pt0[0]):int(pt1[0]) ]                      # 2nd is top-right and 1st is bottom-left
        elif points [0][1] < points [1][1]:                                                         # 1st is above 2nd
            cropped = img [ int(pt0[1]):int(pt1[1]), int(pt0[0]):int(pt1[0]) ]                      # 2nd is bottom-right and 1st is top-left

    cv2.imshow ('cropped', cropped)


cv2.namedWindow ('pic')
cv2.setMouseCallback ('pic', onClick)
cv2.imshow ('pic', img)

cv2.waitKey (0)
