import cv2
import numpy as np

# cropping

'''
img = cv2.imread ('../Images/blue-chicory.jpg')
dim = img.shape

xCenter = int (dim [1] / 2)
yCenter = int (dim [0] / 2)

cropped = img ( xCenter-100:xCenter+100, yCenter-100 : yCenter+100)

cv2.imshow ('pic', img)
cv2.imshow ('pic2', cropped)
cv2.waitKey (0)
'''


# mouse and event capture

'''
def Click (event, x, y, flags, param):
    # print (x, y)

    # if event == cv2.EVENT_LBUTTONDOWN:
    print (x, y)

webcam = cv2.VideoCapture (0)
cv2.namedWindow ('webcam')
cv2.setMouseCallback ('webcam', Click)

while True:
    x, frame = webcam.read ()
    cv2.imshow ('webcam', frame)

    if cv2.waitKey (1) & 0xFF == ord ('q'):
        break
'''


# warping

img = cv2.imread ('../Images/blue-chicory.jpg')

# order of points in pts: top left -> top right -> bottom left -> bottom right

points1 = np.array ([(0, 400), (600, 0), (0, 1150), (600, 750)], np.float32)
points2 = np.array ([(0, 0), (600, 0), (0, 750), (600, 750)], np.float32)

perspective = cv2.getPerspectiveTransform (points1, points2)
warped = cv2.warpPerspective (img, perspective, (600, 750))

cv2.imshow ('pic', warped)
cv2.imshow ('pic2', img)
cv2.waitKey (0)



'''
Assignment:

Q1: Rectify error in that code (which he showed on the session)
    Code: To show RGB color value (?) at the clicked pixel
'''
