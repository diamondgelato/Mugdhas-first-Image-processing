import cv2
import numpy as np

img = np.zeros ((500, 500, 3), np.uint8)

def nothing (x):
    pass

cv2.namedWindow ('hello')

cv2.createTrackbar ('red', 'hello', 0, 255, nothing)
cv2.createTrackbar ('green', 'hello', 0, 255, nothing)
cv2.createTrackbar ('blue', 'hello', 0, 255, nothing)

while True:
    # print (cv2.getTrackbarPos ('bar', 'hello'))

    r = cv2.getTrackbarPos ('red', 'hello')
    g = cv2.getTrackbarPos ('green', 'hello')
    b = cv2.getTrackbarPos ('blue', 'hello')

    img [:] = [b, g, r]

    cv2.imshow ('hello', img)

    if cv2.waitKey (1) & 0xFF == 27:
        break

cv2.destroyAllWindows ()
