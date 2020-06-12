import cv2
import numpy as np

cap = cv2.VideoCapture (0)

def mouse (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (frame[y, x])

cv2.namedWindow ('webcam')
cv2.setMouseCallback ('webcam', mouse)

while True:
    x, frame = cap.read ()
    cv2.imshow ('webcam', frame)

    if cv2.waitKey (1) & 0xFF == ord('q'):
        break
