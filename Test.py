from GenericFeature import *

#logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.DEBUG)
#logger = logging.getLogger('Test')

class Test(GenericFeature):

    def __init__(self, parent, feature, led):
        super().__init__(parent, feature, led)

    def start(self):
        print("Call to method 'start' from child class. Feature is implemented")
        self.led.swithOn()
        
    def stop(self):
        print("Call to method 'stop' from child class. Feature is implemented")
        self.led.swithOff()
    
    def setBinding(self, **args):
        print("Call to method 'setBinding' from child class. Feature is implemented")
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

