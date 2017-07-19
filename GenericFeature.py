import logging
from Configuration import config

isTestMode = config.getboolean('TESTING', 'gpio.emulator')
if(isTestMode):
    from GPIOTest import GPIO
else:
    from RPi import GPIO

class GenericFeature:

    STATE_ON = "ON"
    STATE_OFF = "OFF"
    
    def __new__(cls, parent, feature, led):
        module = __import__(feature)
        my_class = getattr(module, feature)
        return object.__new__(my_class)
    
    def __init__(self, parent, feature, led):
        self.parent = parent
        self.state = GenericFeature.STATE_OFF
        self.led = led
        
    # Methods that will be inherited by child classes    
    def processEvent(self, event):
        if (self.state == GenericFeature.STATE_OFF):
            self.start()
            self.state = GenericFeature.STATE_ON
        elif (self.state == GenericFeature.STATE_ON):
            self.stop()
            self.state = GenericFeature.STATE_OFF
        else:
            raise Exception('Unknow feature state: ' + self.state)
        
    # Methods that will be overrided by child classes
    def setBinding(self, **args):
        logging.warning("Call to method 'setBinding' from generic class. Not implemented for the required feature.")
    
    def start(self):
        logging.warning("Call to method 'start' from generic class. Not implemented for the required feature.")
    
    def stop(self):
        logging.warning("Call to method 'stop' from generic class. Not implemented for the required feature.")
