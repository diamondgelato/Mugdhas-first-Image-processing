import cv2
import numpy as np

img = cv2.imread ('../Images/some-paper-2.jpg')
imgGrey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow ('OG', cv2.WINDOW_NORMAL)

cv2.imshow ('OG', imgGrey)

cv2.namedWindow ('adaptive mean', cv2.WINDOW_NORMAL)
cv2.namedWindow ('global mean', cv2.WINDOW_NORMAL)

ret, globalThresh = cv2.threshold (imgGrey, 15, 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold (imgGrey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 2)
gaussian = cv2.adaptiveThreshold (imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 2)

cv2.imshow ('adaptive mean', adaptive)
cv2.imshow ('global mean', globalThresh)

cv2.waitKey (0)
