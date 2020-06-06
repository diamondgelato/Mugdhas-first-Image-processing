# Show a vertically flipped frame after every 5 seconds using time.time(), from live webcam feed.

import cv2
import time

webcam = cv2.VideoCapture (0)
counter = 0
#last = time.time()

while True:
    x, frame = webcam.read()
    current = time.time()

    if current - last > 5:
        showFrame = cv2.flip(frame, -1)
        last = current
    #else:
        showFrame = frame

    cv2.imshow ('Webcam', frame)
    print ('{0}\n', counter)

    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

    print ('Hello\n')

    counter += 1
