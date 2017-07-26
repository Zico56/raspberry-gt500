import logging
from features.GenericFeature import *

class TestFeature(GenericFeature):

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)

    def start(self):
        logging.debug("Call to method 'start' from child class. Feature is implemented")
        
    def stop(self):
        logging.debug("Call to method 'stop' from child class. Feature is implemented")
    
    def setBinding(self):
        logging.debug("Call to method 'setBinding' from child class. Feature is implemented")
        self.led.label.bind("<Button-1>", self.processEvent)
    
    # Test method for converting image with Pillow
    '''
    def convertPngToJpeg():
        self.image = Image.open("png/rsz_green-led-on-th.png","r")
        self.bg = Image.new('RGB', (25,25), (0,0,0))
        self.text_img = Image.new('RGBA', (25,25), (0, 0, 0, 0))
        self.text_img.paste(self.bg, (0,0))
        self.text_img.paste(self.image, (0,0), mask=self.image)       
        self.text_img.save("jpg/rsz_green-led-on-th.jpg", format="png")
    '''

