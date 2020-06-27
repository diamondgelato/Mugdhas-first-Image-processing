import cv2
import numpy as np

img = cv2.imread ('../Images/some-paper-4.jpg')
imgGrey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow ('OG', cv2.WINDOW_NORMAL)
cv2.namedWindow ('processed', cv2.WINDOW_NORMAL)
cv2.namedWindow ('dilate', cv2.WINDOW_NORMAL)
cv2.namedWindow ('threshold', cv2.WINDOW_NORMAL)
cv2.namedWindow ('cropped', cv2.WINDOW_NORMAL)

kernel = np.ones ((13, 13))

# pre-processing

thresh = cv2.adaptiveThreshold (imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 151, 2)
dilate = cv2.dilate (thresh, kernel)
# dilate = cv2.dilate (imgGrey, kernel)
canny = cv2.Canny (dilate, 100, 200)

# get that page

contours, hierarchy = cv2.findContours (canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

areas = [cv2.contourArea(c) for c in contours]
maxIndex = np.argmax (areas)
maxContour = contours [maxIndex]

# get those points

peri = cv2.arcLength (maxContour, True)
points = [cv2.approxPolyDP (maxContour, 0.01*peri, True)]
print (points)
print (points[0][3][0])

# warp those points

sorted = np.array ([points[0][0][0], points[0][3][0], points[0][1][0], points[0][2][0]], dtype = np.float32)
warpedPoints = np.array ([(0, 0), (750, 0), (0, 750), (750, 750)], dtype = np.float32)

perspective = cv2.getPerspectiveTransform (sorted, warpedPoints)
warped = cv2.warpPerspective (img, perspective, (750, 750))

# cv2.drawContours (img, contours, -1, (255, 255, 0), 1)
cv2.drawContours (img, contours, maxIndex, (0, 255, 0), 1)
cv2.drawContours (img, points, -1, (0, 0, 255), 3)

cv2.imshow ('OG', img)
cv2.imshow ('threshold', thresh)
cv2.imshow ('dilate', dilate)
cv2.imshow ('processed', canny)
cv2.imshow ('cropped', warped)

cv2.waitKey (0)
