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

###### output bit ######
# 01 : head left position/turn indicator    (x1)
# 02 : head right position/turn indicator   (x1)
# 03 : tail left turn indicator #1          (x1)
# 04 : tail left turn indicator #2          (x1)
# 05 : tail left turn indicator #3          (x1)
# 06 : tail right turn indicator #1         (x1)
# 07 : tail right turn indicator #2         (x1)
# 08 : tail right turn indicator #3         (x1)
# 09 : lateral position lights              (x4)
# 10 : tail light                           (x6)
# 11 : head lights                          (x2)
# 12 : fog lights                           (x2)
# 13 : rear license plate (mutualisable?)   (x2)
# 14 : dashboard                            (x2)
# 15 : roof light                           (x1)
# 16 : 

# position light
# fogLights  : 0/1
#

def getlist(option, sep=','):
    return [ int(chunk,16) for chunk in option.split(sep) ]

class ShiftRegister2(GenericFeature):
    
    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        
    def setBinding(self):
        super().setBinding()    
        
        # Get GPIO port to use from configuration
        self.SDI = int(self.featureOptions['GPIO_SDI'])
        self.RCLK = int(self.featureOptions['GPIO_RCLK'])
        self.SRCLK = int(self.featureOptions['GPIO_SRCLK'])     

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

    def start(self):
        logging.info("Starting 74HC595 thread.")
        self.thread = CustomThread(self._74hc595)
        self.thread.start()
        
    def stop(self):
        logging.info("Stopping 74HC595 thread.")
        self.thread.event.set()  
    
    def createLedTemplate(self):
        warning_state = 1/2/3 #TODO: right / left / warning
        if (warning_state == 1):
            pass
        elif (warning_state == 2):
            pass
        elif (warning_state == 1):
            pass
    
    def _74hc595(self):
        # Display template for leds
        ledTemplate = getlist(self.featureOptions['LED_TEMPLATE'])
        
        # Time out delay between two sequence of the led template
        sleeptime = 0.1

        # Iteration on each led sequence
        for i in range(0, len(ledTemplate)):  
        
            # Iteration on each 74HC595 bit/output
            for bit in range(0, 8):  
            
                # Masking and setting state for each 74HC595 output
                GPIO.output(self.SDI, 0x01 & (ledTemplate[i] >> bit))
                GPIO.output(self.SRCLK, GPIO.HIGH)
                time.sleep(0.001)
                GPIO.output(self.SRCLK, GPIO.LOW)

            # Signal to 74HC595 for display output
            GPIO.output(self.RCLK, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(self.RCLK, GPIO.LOW)
            
            # Time out before next sequence
            time.sleep(sleeptime)        
  