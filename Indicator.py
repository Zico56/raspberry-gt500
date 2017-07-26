from tkinter import *
from PIL import Image, ImageTk
from Configuration import config

class Indicator:

    STATE_ON = "ON"
    STATE_OFF = "OFF"

    def __init__(self, parent, imgOnPath, imgOffPath):
        self.state = Indicator.STATE_OFF
        self.imgOn = ImageTk.PhotoImage(Image.open(imgOnPath))
        self.imgOff = ImageTk.PhotoImage(Image.open(imgOffPath))
               
        self.label = Label(parent, image=self.imgOff, bg="black")
        self.label.image = self.imgOff
        self.label.pack()    
        
    def swithOn(self):
        self.label.configure(image=self.imgOn)
        self.state = Indicator.STATE_ON
        
    def swithOff(self):
        self.label.configure(image=self.imgOff)
        self.state = Indicator.STATE_OFF
