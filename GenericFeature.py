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
    
    def __init__(self, parent, feature, led):
        self.parent = parent
        self.state = GenericFeature.STATE_OFF
        self.led = led
        
    # Methods that will be inherited by child classes
    def setGpioEventBinding(self):
        logger.warning("GPIO Event: Not implemented yet.")
        GPIO.add_event_detect(channel, GPIO.FALLING, callback=self.processEvent)
    
    def setLedEventBinding(self):
        self.led.label.bind("<Button-1>", self.processEvent)
        
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
    def start(self):
        logger.warning("Call to method 'start' from generic class. Not implemented for the required feature.")
    
    def stop(self):
        logger.warning("Call to method 'stop' from generic class. Not implemented for the required feature.")
