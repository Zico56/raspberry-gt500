from GenericFeature import *

#logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.DEBUG)
#logger = logging.getLogger('Test')

class Test(GenericFeature):

    def __init__(self, parent, feature, led):
        super().__init__(parent, feature, led)

    def start(self, event):
        print("Call to method from child class. Feature is implemented")
        self.led.changeColor()

