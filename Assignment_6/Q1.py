import cv2
import numpy as np

img = cv2.imread ('../Images/some-paper.jpg')
imgGrey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow ('OG', cv2.WINDOW_NORMAL)
cv2.namedWindow ('canny', cv2.WINDOW_NORMAL)
cv2.namedWindow ('dilate', cv2.WINDOW_NORMAL)
cv2.namedWindow ('threshold', cv2.WINDOW_NORMAL)

kernel = np.ones ((15, 15))

thresh = cv2.adaptiveThreshold (imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 151, 2)
dilate = cv2.dilate (thresh, kernel)
canny = cv2.Canny (dilate, 50, 225)

cv2.imshow ('OG', imgGrey)
cv2.imshow ('threshold', thresh)
cv2.imshow ('dilate', dilate)
cv2.imshow ('canny', canny)
# cv2.imwrite ('../Images/some-paper-edges.jpg', canny)
cv2.waitKey (0)
