# OCR Application Documentation
This is a GUI application which can detect printed text from static pictures. (It's underwhelming I know)
## Installation
### Prerequisites
You need to have the following installed on you PC:
- Python 3.7: [link to download](https://www.python.org/downloads/)
- OpenCV library: [link to download](https://opencv.org/releases/)
- Tesseract OCR library: [link to download](https://tesseract-ocr.github.io/tessdoc/Home.html)
- Tkinter library

Start by downloading the OCRApplication.py file from the OCRApplication folder. 

Open Terminal (for Mac) or Command Prompt (for Windows) and go to the directory where the OCRApplication.py is saved using the `cd` command.

Run the application using the command
`python3 OCRApplication.py`

## Features

##### Broadly the features of this App are:
- Auto Cropping
- Manual Cropping
- Detecting Printed Text
- Showing Text from Picture

##### Auto Cropping

The App can automatically detect and crop a four-sided paper on clicking one button

##### Manual Cropping

The App also allows for cropping the loaded picture manually using mouse clicks to denote the corners of the picture

##### Detecting Printed Text

The App uses the Tesseract OCR APIs to detect the printed text on the input picture and convert to text format which can be used ahead.

##### Showing Text from Picture

The App uses the Tesseract OCR APIs to detect the printed text from the picture and marks the it on the picture, which can be saved for future use.

## User's Manual
##### Starting the Application
Run the application using the command
`python3 OCRApplication.py`
![Start Screen](Mugdhas-first-Image-processing/OCRApplication/Screens/StartScreen.jpeg)

##### Loading pictures in the Application
Click on the 'Open Image' Button and follow the file dialog open an image of your choice.
![Open Image File Dialog](Mugdhas-first-Image-processing/OCRApplication/Screens/OpenImageFileDialog.jpeg)
 
![Open Image Working](Mugdhas-first-Image-processing/OCRApplication/Screens/OpenImageWorking.jpeg)

##### Automatically cropping the picture
If the picture being loaded contains a background which is not needed, it can be cropped out. 
Click the 'Auto Crop' Button to let the App detect the page and crop it 
![Auto Crop Complete](Mugdhas-first-Image-processing/OCRApplication/Screens/AutoCrop.jpeg)

##### Manually cropping the picture
To manually crop the picture, click the manual crop button and directly click the four corners for the cropped image on the image loaded in the order mentioned in the text box. Each corner will be highlighted with a yellow dot after you click it
![Manual Crop](Mugdhas-first-Image-processing/OCRApplication/Screens/ManualCrop1.jpeg)

After all the four clicks are made, the cropped image will open in a new window.
![Manual Crop Complete](Mugdhas-first-Image-processing/OCRApplication/Screens/ManualCropComplete.jepg)

##### Getting the text from the picture
To get the text from the picture, click the 'Detect Text' Button. It will display the text from the picture into the orange text box. The text can then be copied.
![Detect Text](Mugdhas-first-Image-processing/OCRApplication/Screens/DetectText.jpeg)

By clicking on the 'Show Text' Button, bounding boxes are drawn around the text which has been identified
![Show Text](Mugdhas-first-Image-processing/OCRApplication/Screens/ShowText.jpeg)

##### Additional Features
The processed image which is displayed can be saved to your system by clicking the 'Save Image' Button. Clicking this open a dialog box allowing you to save the file at the desired location.
![Save Image](Mugdhas-first-Image-processing/OCRApplication/Screens/SaveImage.jpeg)

All the image can be closed by clicking the 'Close Windows' Button. 
