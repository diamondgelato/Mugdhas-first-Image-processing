import cv2

n = int (input ("Enter the number of frames after which webcam should flip: "))

webcam = cv2.VideoCapture (0)
counter = 0

while True:
    x, frame = webcam.read()

    if counter % n == 0:
        showFrame = cv2.flip (frame, -1)
    else:
        showFrame = frame

    cv2.imshow ('Webcam', showFrame)

    if cv2.waitKey (1) & 0xFF == ord('q'):
        break

    counter += 1
