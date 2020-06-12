# Q3: Get the warped image using four mouse clicks

import cv2
import numpy as np

clicks = np.zeros(shape = (4, 2), dtype = np.float32)
index = 0
img = cv2.imread ('../Images/blue-chicory.jpg')

def onClick (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global index
        global clicks

        if (index < 4):
            clicks[index] = [x, y]
            index += 1

            if np.all (clicks):
                warpImage ()
                print (clicks)
        else:
            pass

def warpImage ():
    global clicks
    topLef = clicks [0]                 # assuming clicks have been made in order top left -> top right -> bottom left -> bottom right
    topRig = clicks [1]
    botLef = clicks [2]
    botRig = clicks [3]

    warpedPoints = np.array ([(0, 0), (750, 0), (0, 750), (750, 750)], dtype = np.float32)

    perspective = cv2.getPerspectiveTransform (clicks, warpedPoints)
    warped = cv2.warpPerspective (img, perspective, (750, 750))

    cv2.imshow ('warped', warped)

cv2.namedWindow ('pic')
cv2.setMouseCallback ('pic', onClick)
cv2.imshow ('pic', img)

cv2.waitKey (0)
