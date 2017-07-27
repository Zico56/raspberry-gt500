import logging
import time
from Configuration import config
from features.GenericFeature import *
from CustomThread import *

################# Raspberry / Emulator mode #################
if(testMode):
    from emulator.GPIOEmulator import GPIO
else:
    from RPi import GPIO
#############################################################

def getlist(option, sep=','):
    return [ int(chunk,16) for chunk in option.split(sep) ]

class ShiftRegister(GenericFeature):
    
    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        
    def setBinding(self):
        super().setBinding()    
        
        # Get GPIO port to use from configuration
        self.SDI = self.featureOptions['GPIO_SDI']
        self.RCLK = self.featureOptions['GPIO_RCLK']
        self.SRCLK = self.featureOptions['GPIO_SRCLK']     

        # Define GPIO as output
        logging.info("Configuring GPIO_" + str(self.SDI) + " as an output.")
        GPIO.setup(self.SDI, GPIO.OUT)
        logging.info("Configuring GPIO_" + str(self.RCLK) + " as an output.")
        GPIO.setup(self.RCLK, GPIO.OUT)
        logging.info("Configuring GPIO_" + str(self.SRCLK) + " as an output.")
        GPIO.setup(self.SRCLK, GPIO.OUT)
        
        # Set GPIO state to LOW
        GPIO.output(self.SDI, GPIO.LOW)
        GPIO.output(self.RCLK, GPIO.LOW)
        GPIO.output(self.SRCLK, GPIO.LOW)


         
  