import cv2
import numpy as np

img = cv2.imread ('../Images/sheep.jpg')
imgGrey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow ('OG', cv2.WINDOW_NORMAL)

cv2.imshow ('OG', imgGrey)

# Thresholding

cv2.namedWindow ('adaptive mean', cv2.WINDOW_NORMAL)
cv2.namedWindow ('global mean', cv2.WINDOW_NORMAL)

ret, globalThresh = cv2.threshold (imgGrey, 15, 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold (imgGrey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 2)
gaussian = cv2.adaptiveThreshold (imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 2)

cv2.imshow ('adaptive mean', adaptive)
cv2.imshow ('global mean', globalThresh)

cv2.waitKey (0)

# Blurring using Kernel Convulsion
# Noise Reduction using Kernel Convulsion

'''
cv2.namedWindow
cv2.namedWindow ('OG', cv2.WINDOW_NORMAL)
cv2.namedWindow ('blurred', cv2.WINDOW_NORMAL)
cv2.namedWindow ('gaussian', cv2.WINDOW_NORMAL)

kernel = np.ones ((25, 25)) / 625
gKernel = np.array ([[1, 2, 1],
                     [2, 4, 2],
                     [1, 2, 1]]) / 16                           # gives higher weightage to the pixels closer to the center

blur = cv2.filter2D (imgGrey, -1, kernel)
# gaussian = cv2.filter2D (imgGrey, -1, gKernel)
gaussian = cv2.

cv2.imshow ('blurred', blur)
cv2.imshow ('gaussian', gaussian)
cv2.waitKey (0)
'''

# Sharpening
'''
cv2.namedWindow ('sharp', cv2.WINDOW_NORMAL)

sharpen =  np.array ([[-1, -1, -1],
                      [-1, 9, -1],
                      [-1, -1, -1]])
sharp = cv2.filter2D (imgGrey, -1, sharpen)

cv2.imshow ('OG', imgGrey)
cv2.imshow ('sharp', sharp)
cv2.waitKey (0)
'''

# Sobel Edge Detection

'''
cv2.namedWindow ('vedges', cv2.WINDOW_NORMAL)
cv2.namedWindow ('hedges', cv2.WINDOW_NORMAL)
cv2.namedWindow ('canny', cv2.WINDOW_NORMAL)

sobelx = np.array ([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
sobely = np.array ([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

vedge = cv2.filter2D (imgGrey, -1, sobelx)
hedge = cv2.filter2D (imgGrey, -1, sobely)

canny = cv2.Canny (imgGrey, 35, 250)

cv2.imshow ('vedges', vedge)
cv2.imshow ('hedges', hedge)
cv2.imshow ('canny', canny)
cv2.waitKey (0)
'''

# Morphological Transformation

'''
# cv2.namedWindow ('erosion', cv2.WINDOW_NORMAL)
# cv2.namedWindow ('dilation', cv2.WINDOW_NORMAL)
cv2.namedWindow ('opening', cv2.WINDOW_NORMAL)
cv2.namedWindow ('closing', cv2.WINDOW_NORMAL)

kernel = np.ones ((3, 3))
eroded = cv2.erode (imgGrey, kernel)
dilate = cv2.dilate (imgGrey, kernel)

opening = cv2.morphologyEx (imgGrey, cv2.MORPH_OPEN, kernel)            # erosion -> dilation
closing = cv2.morphologyEx (imgGrey, cv2.MORPH_CLOSE, kernel)           # dilation -> erosion

# cv2.imshow ('erosion', eroded)
# cv2.imshow ('dilation', dilate)
cv2.imshow ('opening', opening)
cv2.imshow ('closing', closing)
cv2.waitKey (0)
'''
