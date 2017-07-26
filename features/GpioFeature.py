import logging
from Configuration import config
from features.GenericFeature import *

################# Raspberry / Emulator mode #################
if(testMode):
    from emulator.GPIOEmulator import GPIO
else:
    from RPi import GPIO
#############################################################

class GpioFeature(GenericFeature):

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)

    def setBinding(self):
        super().setBinding()        
        self.channelOut = self.featureOptions['GPIO_OUTPUT']
        if (self.channelOut == None) or (self.channelOut == ''):
            raise Exception("No GPIO output defined.")
        self.channelOut = int(self.channelOut)
        
        logging.debug("Configuring GPIO_" + str(self.channelOut) + " as an output.")
        GPIO.setup(self.channelOut, GPIO.OUT)
    
    def start(self): 
        GPIO.output(self.channelOut, GPIO.HIGH)
        
    def stop(self):
        GPIO.output(self.channelOut, GPIO.LOW)
