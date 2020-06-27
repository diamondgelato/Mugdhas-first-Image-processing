import cv2
import numpy as np
import tkinter as tk
import pytesseract
from pytesseract import Output
from tkinter import filedialog
from PIL import ImageTk, Image

img = np.array ([0], dtype = np.uint8)
cropped = np.array ([0], dtype = np.uint8)
display = np.array ([0], dtype = np.uint8)
clicks = np.zeros(shape = (4, 2), dtype = np.float32)
index = 0

def openImage():
    global img

    imgName = filedialog.askopenfilename (initialdir = '/Users/Mugdha/Documents', title = 'Select Image', filetypes = (('JPG', '*.jpg'), ('All files', '*.*')))
    img = cv2.imread (imgName)

    cv2.namedWindow ('OG', cv2.WINDOW_NORMAL)
    cv2.imshow ('OG', img)

def autoCrop():
    global img
    global cropped
    copy = np.copy (img)

    imgGrey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones ((13, 13))

    # pre-processing

    thresh = cv2.adaptiveThreshold (imgGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 151, 2)
    dilate = cv2.dilate (thresh, kernel)
    canny = cv2.Canny (dilate, 100, 200)

    # get that page

    contours, hierarchy = cv2.findContours (canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    areas = [cv2.contourArea(c) for c in contours]
    maxIndex = np.argmax (areas)
    maxContour = contours [maxIndex]

    # get those points

    peri = cv2.arcLength (maxContour, True)
    points = cv2.approxPolyDP (maxContour, 0.03*peri, True)

    # warp those points

    if points.size == 8:
        sumList = [(x[0, 0] + x[0, 1]) for x in points]
        diffList = [(x[0, 0] - x[0, 1]) for x in points]

        minSum = np.argmin (sumList)
        maxSum = np.argmax (sumList)
        minDiff = np.argmin (diffList)
        maxDiff = np.argmax (diffList)

        sorted = np.array ([points[minSum, 0], points[maxDiff, 0], points[minDiff, 0], points[maxSum, 0]], dtype = np.float32)

        warpedPoints = np.array ([(0, 0), (1500, 0), (0, 2000), (1500, 2000)], dtype = np.float32)

        perspective = cv2.getPerspectiveTransform (sorted, warpedPoints)
        warped = cv2.warpPerspective (img, perspective, (1500, 2000))

        cv2.drawContours (copy, contours, maxIndex, (0, 255, 0), 1)
        cv2.drawContours (copy, [points], -1, (0, 0, 255), 3)
        cv2.namedWindow ('copy', cv2.WINDOW_NORMAL)
        cv2.imshow ('copy', copy)

        global display

        display = warped
        displayImage()
        cropped = warped


def manualCrop():
    textFound = 'Click the points of the cropped picture in the following order\n\nTop Left\nTop Right\nBottom Left\nBottom Right'
    text.insert ('1.0', textFound)
    cv2.setMouseCallback ('OG', onClick)


def onClick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global index
        global clicks
        global img

        if (index < 4):
            clicks[index] = [x, y]
            index += 1
            print ('Yeah, you clicked, good job.')
            imgCopy = np.copy (img)
            cv2.circle (imgCopy, (x, y), 25, (0, 255, 255), -1)
            cv2.imshow ('OG', imgCopy)

            if np.all (clicks):
                warpImage ()
        else:
            pass


def warpImage ():
    global clicks
    global img
    global cropped

    topLef = clicks [0]                 # assuming clicks have been made in order top left -> top right -> bottom left -> bottom right
    topRig = clicks [1]
    botLef = clicks [2]
    botRig = clicks [3]

    warpedPoints = np.array ([(0, 0), (1500, 0), (0, 2000), (1500, 2000)], dtype = np.float32)

    perspective = cv2.getPerspectiveTransform (clicks, warpedPoints)
    warped = cv2.warpPerspective (img, perspective, (1500, 2000))

    global display
    display = warped
    displayImage()
    cropped = warped


def getText ():
    global cropped
    global img
    global text

    if cropped.size > 1:
        croppedGrey = cv2.cvtColor (cropped, cv2.COLOR_BGR2GRAY)
    else:
        croppedGrey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold (croppedGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 35)
    textFound = pytesseract.image_to_string(img, lang = 'eng')
    text.delete ('1.0', tk.END)
    text.insert ('1.0', textFound)

    global display
    display = thresh
    displayImage()


def showText ():
    global cropped

    croppedGrey = cv2.cvtColor (cropped, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold (croppedGrey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 201, 35)
    data = pytesseract.image_to_data (thresh, output_type = Output.DICT)
    numberWord = len (data['text'])

    for i in range (numberWord):
        x, y, width, height = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        cv2.rectangle (cropped, (x, y), (x+width, y+height), (255, 0, 0), 1)

    global display
    display = cropped
    displayImage()


def displayImage():
    global display

    # print ('Yea hi! I displayed something')
    cv2.namedWindow ('other', cv2.WINDOW_NORMAL)
    cv2.imshow ('other', display)


def saveImage ():
    global display
    filename = ''
    filename = filedialog.asksaveasfilename (initialdir = '/Users/Mugdha', title = 'Save File', filetypes = (('JPG', '*.jpg'), ('All files','*.*')))
    print (filename)

    if filename != '':
        cv2.imwrite (filename, display)


def closeAllWindows():
    cv2.destroyAllWindows()


def working():
    print ('Yep, this callback works.')


root = tk.Tk ()

canvas = tk.Canvas (root, height = 1000, width = 1000, bg = 'cyan')
canvas.pack()

centerFrame = tk.Frame (canvas, bg = 'white')
centerFrame.place (relx = 0.5, rely = 0.05, relwidth = 0.6, relheight = 0.9, anchor = 'n')

title = tk.Label (centerFrame, text = 'Detected Text', font = ('Helvatica', '30'))
title.place (relx = 0.5, rely = 0.25, anchor = 'n')

text = tk.Text (centerFrame, bg = 'orange')
text.place (relx = 0.5, rely = 0.4, relwidth = 0.75, relheight = 0.5, anchor = 'n')

openImage = tk.Button (canvas, text = 'Open Image', padx = 10, pady = 10, command = openImage)
openImage.place (relx = 0.1, rely = 0.05, anchor = 'n')

autoCrop = tk.Button (canvas, text = 'Auto Crop', padx = 10, pady = 10, command = autoCrop)
autoCrop.place (relx = 0.1, rely = 0.3, anchor = 'n')

manualCrop = tk.Button (canvas, text = 'Manual Crop', padx = 10, pady = 10, command = manualCrop)
manualCrop.place (relx = 0.1, rely = 0.5, anchor = 'n')

saveImage = tk.Button (canvas, text = 'Save Image', padx = 10, pady = 10, command = saveImage)
saveImage.place (relx = 0.1, rely = 0.9, anchor = 'n')

getText = tk.Button (canvas, text = 'Detect Text', padx = 10, pady = 10, command = getText)
getText.place (relx = 0.9, rely = 0.05, anchor = 'n')

showText = tk.Button (canvas, text = 'Show Text', padx = 10, pady = 10, command = showText)
showText.place (relx = 0.9, rely = 0.3, anchor = 'n')

closeWindows = tk.Button (canvas, text = 'Close All Windows', padx = 10, pady = 10, command = closeAllWindows)
closeWindows.place (relx = 0.9, rely = 0.9, anchor = 'n')

root.mainloop ()
