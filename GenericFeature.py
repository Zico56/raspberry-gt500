import logging
from Configuration import testMode

################# Raspberry / Emulator mode #################
if(testMode):
    from GPIOTest import GPIO
else:
    from RPi import GPIO
#############################################################

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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
        self.feature = feature
        if (testMode):
            self.led.label.bind("<Button-1>", self.processEvent)
        
    # Methods that will be inherited by child classes    
    def processEvent(self, event):
        if (self.state == GenericFeature.STATE_OFF):
            self.start()
            self.led.swithOn()
            self.state = GenericFeature.STATE_ON
        elif (self.state == GenericFeature.STATE_ON):
            self.stop()
            self.led.swithOff() 
            self.state = GenericFeature.STATE_OFF
        else:
            raise Exception('Unknow feature state: ' + self.state)
        
    def setBinding(self, **args):
        self.channelIn = args["channel"]
        logging.debug("Configuring GPIO_" + str(self.channelIn) + " as input")
        GPIO.setup(self.channelIn, GPIO.IN)
        GPIO.add_event_detect(self.channelIn, GPIO.RISING, callback=self.processEvent, bouncetime=75)

    # Methods that will be overrided by child classes    
    def start(self):
        logging.warning("Call to method 'start' from generic class. Not implemented for the required feature: " + str(self.feature))
    
    def stop(self):
        logging.warning("Call to method 'stop' from generic class. Not implemented for the required feature: " + str(self.feature))
       
