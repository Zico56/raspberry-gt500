import logging
from tkinter import *
from PIL import Image, ImageTk, ImageDraw

logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.INFO)
logger = logging.getLogger('Led')

class Led:

    imageOff = Image.open("jpg/rsz_red-led-off-th.jpg")
    imageOn = Image.open("jpg/rsz_red-led-on-th.jpg")

    def __init__(self, parent):
        self.state = "OFF"
        
        self.img = ImageTk.PhotoImage(self.imageOff)
        self.label = Label(parent, image=self.img, bg="black")
        self.label.image = self.img
        self.label.bind("<Button-1>", self.callback)
        
        '''
        self.image = Image.open("gif/rsz_red-led-off-th.gif")
        self.photoImage = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(parent, width=25, height=25, bg="white", highlightthickness=0)
        self.canvas.create_image(0, 0, anchor=NW, image=self.photoImage)
        self.canvas.bind("<Button-1>", self.callback)
        '''

    def convertPngToJpeg():
        self.image = Image.open("png/rsz_green-led-on-th.png","r")
        self.bg = Image.new('RGB', (25,25), (0,0,0))
        self.text_img = Image.new('RGBA', (25,25), (0, 0, 0, 0))
        self.text_img.paste(self.bg, (0,0))
        self.text_img.paste(self.image, (0,0), mask=self.image)       
        self.text_img.save("jpg/rsz_green-led-on-th.jpg", format="png")

    def callback(self, event):
        logger.info("callback led")
        self.changeColor()

    def changeColor(self):
        if ( self.state == "OFF"):
            self.img = ImageTk.PhotoImage(self.imageOn)
            self.label.configure(image=self.img)
            self.state = "ON"
        elif ( self.state == "ON"):
            self.img = ImageTk.PhotoImage(self.imageOff)
            self.label.configure(image=self.img)
            self.state = "OFF"
        else:
            raise Exception('Unknow led state')
