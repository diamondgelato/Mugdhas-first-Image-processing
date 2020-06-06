# Strike off an image using image.shape and drawing tools.

import cv2

img = cv2.imread ('../Images/blue-chicory.jpg')
size = img.shape

cv2.line (img, (0,0), (size[1],size[0]), (0, 0, 0), 3)

cv2.imshow ('Image', img)
cv2.waitKey (0)
