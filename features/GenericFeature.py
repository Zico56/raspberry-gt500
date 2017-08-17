import logging
from importlib import import_module
from Configuration import config
from Configuration import testMode
from Indicator import Indicator

################# Raspberry / Emulator mode #################
if(testMode):
    from emulator.GPIOEmulator import GPIO
else:
    from RPi import GPIO
#############################################################

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class GenericFeature:

    STATE_ON = "ON"
    STATE_OFF = "OFF"
    
    indicator = None
    
    def __new__(cls, parent, configSection):
        featureOptions = dict(config.items(configSection))
        moduleName = featureOptions['MODULE_NAME']
        module = import_module('features.' + moduleName)
        my_class = getattr(module, moduleName)
        my_object = object.__new__(my_class)
        my_object.featureOptions = featureOptions
        return my_object
    
    def __init__(self, parent, configSection):
        self.parent = parent
        self.configSection = configSection
        
        # Default feature state is OFF
        self.state = GenericFeature.STATE_OFF
        
        # Indicator initialization
        indicImgOnPath = self.featureOptions['INDIC_ON_IMG']
        indicImgOffPath = self.featureOptions['INDIC_OFF_IMG']        
        self.indicator = Indicator(parent, indicImgOnPath, indicImgOffPath)

        # Event binding
        self.setBinding()        
        
    # Methods that will be inherited by child classes    
    def processEvent(self, event):
        if (self.state == GenericFeature.STATE_OFF):
            self.start()
            self.indicator.swithOn() 
            self.state = GenericFeature.STATE_ON
        elif (self.state == GenericFeature.STATE_ON):
            self.stop()
            self.indicator.swithOff() 
            self.state = GenericFeature.STATE_OFF
        else:
            raise Exception('Unknown feature state: ' + self.state)
        
    def setBinding(self):
        # Mouse event binding
        self.indicator.label.bind("<Button-1>", self.processEvent)

    # Methods that will be overrided by child classes    
    def start(self):
        logging.warning("Call to method 'start' from generic class. Not implemented for the required feature: " + self.featureOptions['MODULE_NAME'])
    
    def stop(self):
        logging.warning("Call to method 'stop' from generic class. Not implemented for the required feature: " + self.featureOptions['MODULE_NAME'])
       
