# Select a template from the webcam live feed using two clicks (like the
# cropping one). After selecting the template, track that object in the webcam
# by making a bounding box around it

'''
Ok so what's the plan

- (done) crop the object and save it as a template
- match the template and get the point where the object is
- draw a box and write text around it
'''

import cv2
import numpy as np

template = np.ndarray (shape = (0, 0), dtype = np.uint8)
webcam = cv2.VideoCapture (0)
index = 0
points = np.zeros (shape = (2, 2), dtype = int)

# records the clicks for the object

def onClick (event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global index
        global points
        global template

        if (index < 2):
            points[index] = [y, x]
            index = index + 1

            if np.all (points):
                template = cropImage (webcam.read() [1], points)
        else:
            pass

# crops image and makes the template according to the points

def cropImage (still, pts):
    pt0 = pts[0]
    yPt0 = int(pt0[0])
    xPt0 = int(pt0[1])
    pt1 = pts[1]
    yPt1 = int(pt1[0])
    xPt1 = int(pt1[1])

    if pts [0][0] > pts [1][0]:                                                               # 1st is to below of 2nd
        if pts [0][1] > pts [1][1]:                                                           # 1st is right of 2nd
            cropped = still [ yPt1:yPt0, xPt1:xPt0 ]                      # 2nd is top-left and 1st is bottom-right
        elif pts [0][1] < pts [1][1]:                                                         # 1st is left of 2nd
            cropped = still [ yPt1:yPt0, xPt0:xPt1 ]                      # 2nd is bottom-left and 1st is top-right
    elif pts [0][0] < pts [1][0]:                                                             # 1st is above of 2nd
        if pts [0][1] > pts [1][1]:                                                           # 1st is right of 2nd
            cropped = still [ yPt0:yPt1, xPt1:xPt0 ]                      # 2nd is top-right and 1st is bottom-left
        elif pts [0][1] < pts [1][1]:                                                         # 1st is left of 2nd
            cropped = still [ yPt0:yPt1, xPt0:xPt1 ]                      # 2nd is bottom-right and 1st is top-left

    return cropped

# matches each still with the template

def compareImage (still):
    global template
    greystill = cv2.cvtColor (still, cv2.COLOR_BGR2GRAY)
    greyTemplate = cv2.cvtColor (template, cv2.COLOR_BGR2GRAY)

    match = cv2.matchTemplate (greystill, greyTemplate, cv2.TM_CCOEFF_NORMED)

    loc = np.where (match > 0.8)
    print (loc)

    return loc


cv2.namedWindow ('webcam', cv2.WINDOW_NORMAL)
cv2.setMouseCallback ('webcam', onClick)

while True:
    x, frame = webcam.read ()

    if template.size > 3:
        width = template.shape [1]
        height = template.shape [0]
        matches = compareImage (frame)

        for x, y in zip (*matches [::-1]):
            # cv2.putText (frame, 'Object', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.rectangle (frame, (x, y), (x+width, y+height), (255, 255, 255), 1)

        cv2.imshow ('object', template)

    cv2.imshow ('webcam', frame)

    if cv2.waitKey (20) & 0xFF == 27:
        break
