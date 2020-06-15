import cv2

webcam = cv2.VideoCapture (0)
counter = 0

while True:
    x, frame = webcam.read ()

    if counter % 2 == 0:
        showFrame = cv2.flip (frame, 1)
    else:
        showFrame = frame

    cv2.imshow ('Webcam', showFrame)

    if cv2.waitKey (1000) & 0xFF == ord ('q'):
        break

    counter += 1
