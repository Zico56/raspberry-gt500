from tkinter import *
from PIL import Image, ImageTk, ImageDraw

class Led:

    imageOff = Image.open("jpg/rsz_red-led-off-th.jpg")
    imageOn = Image.open("jpg/rsz_red-led-on-th.jpg")
    
    STATE_ON = "ON"
    STATE_OFF = "OFF"

    def __init__(self, parent):
        self.state = Led.STATE_OFF
        self.img = ImageTk.PhotoImage(Led.imageOff)
        self.label = Label(parent, image=self.img, bg="black")
        self.label.image = self.img        
        '''
        self.image = Image.open("gif/rsz_red-led-off-th.gif")
        self.photoImage = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(parent, width=25, height=25, bg="white", highlightthickness=0)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photoImage)
        self.canvas.bind("<Button-1>", self.callback)
        '''
        
    def swithOn(self):
        self.img = ImageTk.PhotoImage(Led.imageOn)
        self.label.configure(image=self.img)
        self.state = Led.STATE_ON
        
    def swithOff(self):
        self.img = ImageTk.PhotoImage(Led.imageOff)
        self.label.configure(image=self.img)
        self.state = Led.STATE_OFF

    # deprecated: use swithOn/swithOff methods instead
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
