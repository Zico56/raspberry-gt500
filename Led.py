from tkinter import *
from PIL import Image, ImageTk
from Configuration import config

class Led:

    imageOn = Image.open(config.get('APPLICATION', 'LED_ON_IMG'))
    imageOff = Image.open(config.get('APPLICATION', 'LED_OFF_IMG'))
    
    STATE_ON = "ON"
    STATE_OFF = "OFF"

    def __init__(self, parent):
        self.state = Led.STATE_OFF
        self.img = ImageTk.PhotoImage(Led.imageOff)
        self.label = Label(parent, image=self.img, bg="black")
        self.label.image = self.img
        self.label.pack()    
        
    def swithOn(self):
        self.img = ImageTk.PhotoImage(Led.imageOn)
        self.label.configure(image=self.img)
        self.state = Led.STATE_ON
        
    def swithOff(self):
        self.img = ImageTk.PhotoImage(Led.imageOff)
        self.label.configure(image=self.img)
        self.state = Led.STATE_OFF

    # deprecated: use swithOn/swithOff methods instead
    '''
    def changeColor(self):
        if ( self.state == "OFF"):
            self.img = ImageTk.PhotoImage(Led.imageOn)
            self.label.configure(image=self.img)
            self.state = "ON"
        elif ( self.state == "ON"):
            self.img = ImageTk.PhotoImage(Led.imageOff)
            self.label.configure(image=self.img)
            self.state = "OFF"
        else:
            raise Exception('Unknow led state')
    '''
