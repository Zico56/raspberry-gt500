import logging
import threading
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

    def start(self):
        logging.info("Starting 74HC595 thread.")
        self.thread = CustomThread(self._74hc595)
        self.thread.start()
        
    def stop(self):
        logging.info("Stopping 74HC595 thread.")
        self.thread.event.set()  
    
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
  