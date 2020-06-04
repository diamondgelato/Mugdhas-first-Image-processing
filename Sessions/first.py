import cv2
# img = cv2.imread('Images/pom-pom.jpg')    # import image into the file
# print(img)                                # prints all the pixels in the image
# cv2.imshow('Pom Pom', img)                # shows image on the screen
# cv2.waitKey(0)                            # waits until a key is pressed to continue program

webcam = cv2.VideoCapture(0)                # captures the live feed from the inbulit webcam (denoted by 0)
counter = 0

while True:
    x, frame = webcam.read()                # saves indivisual frames from the webcam to frame
    # cv2.imshow ('Webcam', frame)          # displays the frames continuously to form a video
    if counter % 2 == 0:
        showFrame = cv2.flip (frame, -1)    # flips the frame based on counter value
    else:
        showFrame = frame

    cv2.imshow ('Webcam', showFrame)

    if cv2.waitKey (250) & 0xFF == ord('q'):  # compares the key pressed to 'q'
        break                               # webcam stops if 'q' is pressed

    counter+=1
