import logging

logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.DEBUG)
logger = logging.getLogger('GenericFeature')

class GenericFeature:

    STATE_ON = "ON"
    STATE_OFF = "OFF"
    
    def __new__(cls, parent, feature, led):
        module = __import__(feature)
        my_class = getattr(module, feature)
        return object.__new__(my_class)
        #instance = my_class()
        #print("Type:" + str(type(instance)))
    
    def __init__(self, parent, feature, led):
        self.parent = parent
        self.state = GenericFeature.STATE_OFF
        self.led = led
        self.led.label.bind("<Button-1>", self.start)

    def start(self, event):
        print("Call to method from generic class. Not implemented for the required feature.")
    
    def stop(self):
        print("Call to method from generic class. Not implemented for the required feature.")
