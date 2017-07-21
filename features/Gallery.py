import logging
from tkinter import *
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile, join, splitext
from features.GenericFeature import *
from Configuration import config

class Gallery(GenericFeature):

    galleryPath = config.get('GALLERY', 'GALLERY_PATH')
    imageLeft = Image.open(config.get('GALLERY', 'LEFT_INDIC_PATH'))
    imageRight = Image.open(config.get('GALLERY', 'RIGHT_INDIC_PATH'))    

    def __init__(self, parent, feature, led):
        super().__init__(parent, feature, led)
        self.parent = parent
        self.createGalleryPanel()        

    # Overrided methods   
    def start(self):
        self.panel.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.panel.focus_set()
        
    def stop(self):
        self.panel.place_forget()

    # Class methods
    def createGalleryPanel(self):
        self.panel = PanedWindow(self.parent, orient=HORIZONTAL, bg="black")

        imgLeft = ImageTk.PhotoImage(self.imageLeft)
        self.labelLeft = Label(self.panel, image=imgLeft, bg="black")
        self.labelLeft.image = imgLeft
        self.panel.add(self.labelLeft)
        
        size = 150,150
        imageTest = Image.open("gallery/test_img_1.jpg")
        imageTest.thumbnail(size,Image.ANTIALIAS)
        imgTest = ImageTk.PhotoImage(imageTest)
        labelTest = Label(self.panel, image=imgTest, bg="black", anchor='center')
        labelTest.image = imgTest
        self.panel.add(labelTest)        

        imgRight = ImageTk.PhotoImage(self.imageRight)
        self.labelRight = Label(self.panel, image=imgRight, bg="black")
        self.labelRight.image = imgRight
        self.panel.add(self.labelRight)
        
        self.panel.bind("<Key>", self.callback)
        self.panel.bind("<KeyRelease>", self.callback)
        
    def callback(self, event):
        if (event.type == "2"):
            if (event.keysym == "Left"):
                imgLeft = ImageTk.PhotoImage(Image.open("jpg/left_on.jpg"))
                self.labelLeft.configure(image=imgLeft)
                self.labelLeft.image = imgLeft
                # TODO: display previous image
            elif (event.keysym == "Right"):
                imgRight = ImageTk.PhotoImage(Image.open("jpg/right_on.jpg"))
                self.labelRight.configure(image=imgRight)
                self.labelRight.image = imgRight
                # TODO: display next image
        elif (event.type == "3"):
            if (event.keysym == "Left"):
                imgLeft = ImageTk.PhotoImage(Image.open("jpg/left_off.jpg"))
                self.labelLeft.configure(image=imgLeft)
                self.labelLeft.image = imgLeft
            elif (event.keysym == "Right"):
                imgRight = ImageTk.PhotoImage(Image.open("jpg/right_off.jpg"))
                self.labelRight.configure(image=imgRight)
                self.labelRight.image = imgRight

    def listFiles():
        for f in listdir(self.galleryPath):
            print(isfile(join(self.galleryPath, f)))
            print(str(f))
            extension = splitext(f)[1]
            print("extension:" + extension)