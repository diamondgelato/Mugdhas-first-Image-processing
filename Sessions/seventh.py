import cv2
import numpy as np

img = cv2.imread ('../Images/blue-chicory.jpg')
hsvImg = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)

cv2.imshow ('OG', img)

# masking and colour filtering

lowerbound = np.array ([])
upperbound = np.array ([180, 255, 255])

mask = cv2.inRange (hsvImg, lowerbound, upperbound)
result = cv2.bitwise_and (img, img, mask = mask)

# getting contours

contours, hierarchy = cv2.findContours (mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# finding biggest contour

areas = [cv2.contourArea(c) for c in contours]
maxIndex = np.argmax (areas)
maxContour = contours [maxIndex]

# making a bounding box around biggest contour

x, y, width, height = cv2.boundingRect(maxContour)
cv2.rectangle (img, (x, y), (x+width, y+height), (0, 0, 0), 2)

# approximating the shape of contour

perimeter = cv2.arcLength (maxContour, True)
ROI = cv2.approxPolyDP (maxContour, 0.01*perimeter, True)

# drawing a convex shape around the contour

hull = cv2.convexHull (maxContour)

cv2.drawContours (img, contours, -1, (0, 0, 0), 3)
cv2.drawContours (img, maxContour, -1, (0, 0, 0), 3)
cv2.drawContours (img, ROI, -1, (0, 0, 0), 3)

cv2.imshow ('masked', result)
cv2.waitKey (0)
