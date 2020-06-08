# Using loops, fill an image with randomly coloured, equal sized squares. Square dimensions:
# width = (image width)/7, height = (image height)/7.

import cv2
import numpy as np
import random

img = cv2.imread ('../Images/blue-chicory.jpg')
dimensions = img.shape
yUnit = dimensions[0] / 7
xUnit = dimensions[1] / 7

for x in range (1, 8):
    xStart = int(xUnit * (x-1))
    xEnd = int(xUnit * x)

    for y in range (1, 8):
        yStart = int(yUnit * (y-1))
        yEnd = int(yUnit * y)

        img [ yStart:yEnd, xStart:xEnd ] = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))

cv2.imshow ('coloured box bois', img)
cv2.waitKey (0)
