import tkinter as tk
from tkinter import filedialog,Text
from PIL import Image,ImageTk

def clicked ():
    # print ('clicked me!')

    # stores file path
    filename = filedialog.askopenfilename (initialdir = '/Users/Mugdha', title = 'Select File', filetypes = (('JPG', '*.jpg'), ('All files','*.*')))
    print (filename)

    '''
    # makes the image readable in tkinter
    img = ImageTk.PhotoImage (Image.open(filename))
    tile = tk.Label (frame, image = img)
    tile.image = img
    tile.place(relx = 0.2, rely = 0.2, relwidth = 0.6, relheight = 0.6)
    '''

def showText ():
    textBox = tk.Frame (frame, bg = 'cyan')
    textBox.place (relx = 0.2, rely = 0.2, relwidth = 0.6, relheight = 0.6)

    text = Text (textBox, bg = 'cyan')
    text.insert ('1.0', 'Hellu!')
    text.pack ()

root = tk.Tk ()

canvas = tk.Canvas (root, height = 800, width = 800, bg = 'blue')
canvas.pack()

frame = tk.Frame (canvas, bg = 'orange')
frame.place (relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)

clickme = tk.Button (frame, text = 'Show Text', fg = 'blue', padx = 10, pady = 10, command = showText)
clickme.pack()

root.mainloop()
