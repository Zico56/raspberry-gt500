import logging
from tkinter import *
from PIL import Image, ImageTk

logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.INFO)
logger = logging.getLogger('Gallery')

class Gallery:

    imageLeft = Image.open("jpg/left_off.jpg")
    imageRight = Image.open("jpg/right_off.jpg")
    
    def __init__(self, parent):
        self.panel = PanedWindow(parent, orient=HORIZONTAL, bg="black", height=45, width=300)

        imgLeft = ImageTk.PhotoImage(self.imageLeft)
        self.labelLeft = Label(self.panel, image=imgLeft, bg="black",anchor=W)
        self.labelLeft.image = imgLeft
        self.panel.add(self.labelLeft)

        self.panel.add(Label(self.panel, text='Gallery', background='green'))

        imgRight = ImageTk.PhotoImage(self.imageRight)
        self.labelRight = Label(self.panel, image=imgRight, bg="black", anchor=E)
        self.labelRight.image = imgRight
        self.panel.add(self.labelRight)

    def callback(self, event):
        if (event.type == "2"):
            if (event.keysym == "Left"):
                imgLeft = ImageTk.PhotoImage(Image.open("jpg/left_on.jpg"))
                self.labelLeft.configure(image=imgLeft)
                self.labelLeft.image = imgLeft
            elif (event.keysym == "Right"):
                imgRight = ImageTk.PhotoImage(Image.open("jpg/right_on.jpg"))
                self.labelRight.configure(image=imgRight)
                self.labelRight.image = imgRight
        elif (event.type == "3"):
            if (event.keysym == "Left"):
                imgLeft = ImageTk.PhotoImage(Image.open("jpg/left_off.jpg"))
                self.labelLeft.configure(image=imgLeft)
                self.labelLeft.image = imgLeft
            elif (event.keysym == "Right"):
                imgRight = ImageTk.PhotoImage(Image.open("jpg/right_off.jpg"))
                self.labelRight.configure(image=imgRight)
                self.labelRight.image = imgRight