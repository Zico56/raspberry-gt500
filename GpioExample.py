import logging
from Configuration import config
from GenericFeature import *

################# Raspberry / Emulator mode #################
if(testMode):
    from GPIOTest import GPIO
else:
    from RPi import GPIO
#############################################################

class GpioExample(GenericFeature):

    def __init__(self, parent, feature, led):
        super().__init__(parent, feature, led)

    def setBinding(self, **args):
        super().setBinding(**args)
        
        self.channelOut = config.get('GPIO_OUTPUT', str(self.channelIn))
        #print("channelIn: " + str(self.channelIn))
        #print("channelOut: " + str(self.channelOut))
        
        logging.debug("Configuring GPIO_" + str(self.channelOut) + "as output")
        #GPIO.setup(self.channelOut, GPIO.OUT)
    
    def start(self):  
        pass
        #GPIO.output(self.channelOut, GPIO.HIGH)
        
    def stop(self):
        pass
        #GPIO.output(self.channelOut, GPIO.LOW)
