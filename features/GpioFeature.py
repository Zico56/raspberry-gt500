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

    def __init__(self, parent, feature, led):
        super().__init__(parent, feature, led)

    def setBinding(self, **args):
        super().setBinding(**args)        
        self.channelOut = config.getint('GPIO_OUTPUT', str(self.channelIn))
        logging.debug("Configuring GPIO_" + str(self.channelOut) + "as output")
        GPIO.setup(self.channelOut, GPIO.OUT)
    
    def start(self): 
        GPIO.output(self.channelOut, GPIO.HIGH)
        
    def stop(self):
        GPIO.output(self.channelOut, GPIO.LOW)
