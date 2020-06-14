import cv2
import numpy as np

still = cv2.imread ('../Images/repeating-sheep.jpg')
template = cv2.imread ('../Images/sheep.jpg')

greystill = cv2.cvtColor (still, cv2.COLOR_BGR2GRAY)
greyTemplate = cv2.cvtColor (template, cv2.COLOR_BGR2GRAY)

match = cv2.matchTemplate (greystill, greyTemplate, cv2.TM_CCOEFF_NORMED)

cv2.imshow ('comparison', match)
cv2.waitKey (0)
