# Inverts 3-channel RGB pictures

import cv2
import numpy as np

img = cv2.imread ('../Images/blue-chicory.jpg')
dimensions = img.shape

inverted = (255 * np.ones ((img.shape[0], img.shape[1], 3), np.uint8)) - img

cv2.imshow ('normal boi', img)
cv2.imshow ('inverted boi', inverted)
cv2.waitKey (0)
