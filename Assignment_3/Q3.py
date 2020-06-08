# Using loops, move a square block throughout the image in the following manner:
# i) left to right for even numbered row.
# ii) right to left for odd numbered row.
# iii) Introduce a delay of 0.5 second, so that the motion of the square is visible.
# Dimensions of the square are the same as in question 1.

import cv2
import random

img = cv2.imread ('../Images/space-1.jpg')
dimensions = img.shape
yUnit = dimensions[0] / 7
xUnit = dimensions[1] / 7

for y in range (1, 8):
    yStart = int(yUnit * (y-1))
    yEnd = int(yUnit * y)

    if y % 2 == 0:
        start = 1
        end = 8
        step = 1
    elif y % 2 != 0:
        start = 7
        end = 0
        step = -1

    for x in range (start, end, step):
        xStart = int(xUnit * (x-1))
        xEnd = int(xUnit * x)

        img = cv2.imread ('../Images/space-1.jpg')
        img [ yStart:yEnd, xStart:xEnd ] = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))

        cv2.imshow ('moving box', img)
        cv2.waitKey(500)


cv2.waitKey (0)
