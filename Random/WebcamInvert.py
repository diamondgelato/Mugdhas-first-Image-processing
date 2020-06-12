import cv2
import numpy as np

webcam = cv2.VideoCapture (0)
# img = cv2.imread ('../Images/blue-chicory.jpg')

while True:
    x, img = webcam.read ()
    dimensions = img.shape

    inverted = (255 * np.ones ((img.shape[0], img.shape[1], 3), np.uint8)) - img

# cv2.imshow ('normal boi', img)
    cv2.imshow ('inverted boi', inverted)

    if cv2.waitKey (1) & 0xFF == ord ('q'):
        break
