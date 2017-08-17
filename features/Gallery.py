import logging
import threading
import time
from tkinter import *
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile, join, splitext
from features.GpioFeature import *
from CustomThread import *
from Configuration import config

class Gallery(GpioFeature):

    currentImage = None

    # Path to images directory for the gallery
    galleryPath = config.get('GALLERY', 'GALLERY_PATH')
    
    # Left arrow on/off images
    leftImgOn = Image.open(config.get('GALLERY', 'LEFT_ARROW_ON'))
    leftImgOff = Image.open(config.get('GALLERY', 'LEFT_ARROW_OFF'))
    
    # Right arrow on/off images
    rightImgOn = Image.open(config.get('GALLERY', 'RIGHT_ARROW_ON'))     
    rightImgOff = Image.open(config.get('GALLERY', 'RIGHT_ARROW_OFF'))   

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        self.createGalleryPanel()               

    # Overrided methods   
    def start(self):
        super().start()
        self.panel.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.panel.focus_set()
        self.thread = CustomThread(self.scrollImage)
        self.thread.event.clear()
        self.thread.start()
        
    def stop(self):
        super().stop()
        self.panel.place_forget()
        self.thread.event.set()  

    # Class methods
    def createGalleryPanel(self):
        self.panel = PanedWindow(self.parent.winfo_toplevel(), orient=HORIZONTAL, bg="black")

        # left arrow
        imgLeft = ImageTk.PhotoImage(self.leftImgOff)
        self.labelLeft = Label(self.panel, image=imgLeft, bg="black")
        self.labelLeft.image = imgLeft
        
        # right arrow
        imgRight = ImageTk.PhotoImage(self.rightImgOff)
        self.labelRight = Label(self.panel, image=imgRight, bg="black")
        self.labelRight.image = imgRight    
        
        # gallery image
        self.labelImage = Label(self.panel, bg="black", anchor='center')
        self.setImageToDisplay(0)
        self.displayPanelImage()
        
        # panel construction
        #self.panel.add(self.labelLeft)
        self.panel.add(self.labelImage)       
        #self.panel.add(self.labelRight)
        self.panel.bind("<Key>", self.callback)
        self.panel.bind("<KeyRelease>", self.callback)
        
    def callback(self, event):
        if (event.type == "2"):
            if (event.keysym == "Left"):
                imgLeft = ImageTk.PhotoImage(self.leftImgOn)
                self.labelLeft.configure(image=imgLeft)
                self.labelLeft.image = imgLeft
                self.showPreviousImage()
            elif (event.keysym == "Right"):
                imgRight = ImageTk.PhotoImage(self.rightImgOn)
                self.labelRight.configure(image=imgRight)
                self.labelRight.image = imgRight
                self.showNextImage()
        elif (event.type == "3"):
            if (event.keysym == "Left"):
                imgLeft = ImageTk.PhotoImage(self.leftImgOff)
                self.labelLeft.configure(image=imgLeft)
                self.labelLeft.image = imgLeft
            elif (event.keysym == "Right"):
                imgRight = ImageTk.PhotoImage(self.rightImgOff)
                self.labelRight.configure(image=imgRight)
                self.labelRight.image = imgRight
            
    def displayPanelImage(self):
        size = 600,370
        image = Image.open(self.galleryPath + self.currentImage)
        image.thumbnail(size,Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        self.labelImage.configure(image=img)
        self.labelImage.image = img 
    
    def scrollImage(self):
        self.showNextImage()
        time.sleep(2)
    
    def showNextImage(self):
        self.setImageToDisplay(1)
        self.displayPanelImage()
        
    def showPreviousImage(self):
        self.setImageToDisplay(-1)
        self.displayPanelImage()
    
    def setImageToDisplay(self, rank):
        fileList = listdir(self.galleryPath)
        for file in fileList:
            if not file.endswith(".jpg"):
                fileList.remove(file)
        
        if (self.currentImage == None):
            fileIdx = 0 
        else:
            for i, file in enumerate(fileList):
                if (self.currentImage == file):
                    fileIdx = i + rank
                    if (fileIdx+1 > len(fileList)):
                        fileIdx = 0
                    elif (fileIdx < 0):
                        fileIdx = len(fileList)-1
                    break

        self.currentImage = fileList[fileIdx]
