# Show a vertically flipped frame after every 5 seconds using time.time(), from live webcam feed.

import cv2
import time

webcam = cv2.VideoCapture (0)
last = time.time()

while True:
    x, frame = webcam.read()
    current = time.time()

    if (current - last) > 2:
        showFrame = cv2.flip (frame, -1)
        last = current
    else:
        showFrame = frame

    cv2.imshow ('Webcam', showFrame)
    print ((last, current))

    if cv2.waitKey (1) & 0xFF == ord ('q'):
        break
