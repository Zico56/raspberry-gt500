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

#SDI = 17
#RCLK = 18
#SRCLK = 27

def getlist(option, sep=','):
    return [ int(chunk,16) for chunk in option.split(sep) ]

    '''
class ShiftRegisterThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.event = threading.Event()

    def run(self):    
        ledTemplate = getlist(config.get('FEATURE_3', 'LED_TEMPLATE'))
        #ledTemplate = [0x00,0x18,0x24,0x42,0x81,0x42,0x24,0x18]
        sleeptime = 0.5
        while not self.event.is_set():
            for i in range(0, len(ledTemplate)):          
                self.hc595_in(ledTemplate[i])
                self.hc595_out()
                time.sleep(sleeptime)        
    
    def hc595_in(self, dat):
        for bit in range(0, 8):  
            GPIO.output(SDI, 0x01 & (dat >> bit))
            GPIO.output(SRCLK, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(SRCLK, GPIO.LOW)
    
    def hc595_out(self):
        GPIO.output(RCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(RCLK, GPIO.LOW)
'''

class ShiftRegister(GenericFeature):
    
    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        
    def setBinding(self):
        super().setBinding()    
        
        self.SDI = self.featureOptions['GPIO_SDI']
        self.RCLK = self.featureOptions['GPIO_RCLK']
        self.SRCLK = self.featureOptions['GPIO_SRCLK']     

        # Define GPIO as output
        logging.info("Configuring GPIO_" + str(SDI) + " as an output.")
        GPIO.setup(SDI, GPIO.OUT)
        logging.info("Configuring GPIO_" + str(RCLK) + " as an output.")
        GPIO.setup(RCLK, GPIO.OUT)
        logging.info("Configuring GPIO_" + str(SRCLK) + " as an output.")
        GPIO.setup(SRCLK, GPIO.OUT)
        
        # Set GPIO state to LOW
        GPIO.output(SDI, GPIO.LOW)
        GPIO.output(RCLK, GPIO.LOW)
        GPIO.output(SRCLK, GPIO.LOW)

    def start(self):
        logging.info("Starting 74HC595 thread.")
        #self.thread = ShiftRegisterThread()
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

        for i in range(0, len(ledTemplate)):  
            for bit in range(0, 8):  
                GPIO.output(self.SDI, 0x01 & (ledTemplate[i] >> bit))
                GPIO.output(self.SRCLK, GPIO.HIGH)
                time.sleep(0.001)
                GPIO.output(self.SRCLK, GPIO.LOW)

                GPIO.output(self.RCLK, GPIO.HIGH)
                time.sleep(0.001)
                GPIO.output(self.RCLK, GPIO.LOW)
            time.sleep(sleeptime)        
    
    '''
    def hc595_in(self, dat):
        for bit in range(0, 8):  
            GPIO.output(SDI, 0x01 & (dat >> bit))
            GPIO.output(SRCLK, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(SRCLK, GPIO.LOW)
    
    def hc595_out(self):
        GPIO.output(RCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(RCLK, GPIO.LOW)
     '''   
        