import cv2
import numpy as np
import random

template = cv2.imread ('../Images/sheep.jpg')
greyTemplate = cv2.cvtColor (template, cv2.COLOR_BGR2GRAY)                              # IP requires the object and template to be in greyscale for template matching
img = cv2.imread ('../Images/repeating-sheep.jpg')
greyImg = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

width = template.shape [1]                                                              # to get dimensions for the bounding box
height = template.shape [0]

res = cv2.matchTemplate (greyImg, greyTemplate, cv2.TM_CCOEFF_NORMED)                   # returns an image with pixel value of the matched areas near 1

loc = np.where ( res > 0.95 )                                                           # returns arrays of x and y coordinates respectively which satisfy the condition

for x, y in zip (*loc [::-1]):
    cv2.putText (img, 'Sheep', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 1)
    cv2.rectangle (img, (x, y), (x+width, y+height), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 1)                               # draw the bounding boxes


cv2.imshow ('pic', img)
cv2.waitKey (0)


'''
Some Notes:

- the coordinates returned by matchTemplate are the top left corners of the matched parts of the Images
- There are three types of ways to match but TM_CCOEFF_NORMED is the best for us, but do check out the others
'''
