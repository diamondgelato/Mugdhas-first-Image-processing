import cv2
import numpy as np
import pytesseract
from pytesseract import Output

cv2.namedWindow ('image', cv2.WINDOW_NORMAL)
cv2.namedWindow ('Image', cv2.WINDOW_NORMAL)

img = cv2.imread ('../Images/some-paper-3.jpg')

# converts the text on the picture to string object

text = pytesseract.image_to_string(img, lang = 'eng')
print (text)

# gets the words, their location and other info regarding the picture

data = pytesseract.image_to_data (img, output_type = Output.DICT)
numberWord = len (data['text'])
# print (numberWord)

for i in range (numberWord):
    if int(data['conf'][i]) > 50:
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        # cv2.putText (img, data ['text'][i], (x, y), )
        cv2.rectangle (img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow ('Image', img)
        cv2.waitKey (100)                                                       # animation!

    '''
    if str(data['text'][i]) == 'Safety':                                                        # to black out some particular text
        cv2.rectangle (img, (x, y), (x+w, y+h), (255, 0, 0), -1)
    '''

cv2.imshow ('image', img)
cv2.waitKey (0)
