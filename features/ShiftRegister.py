import logging
from Configuration import config
from features.GenericFeature import *

################# Raspberry / Emulator mode #################
if(testMode):
    from emulator.GPIOEmulator import GPIO
else:
    from RPi import GPIO
#############################################################

class ShiftRegister(GenericFeature):



    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        
    def setBinding(self):
        super().setBinding()    

        SDI   = 17
        RCLK  = 18
        SRCLK = 27        

        #GPIO.setmode(GPIO.BOARD)    # Number GPIOs by its physical location
        GPIO.setup(SDI, GPIO.OUT)
        GPIO.setup(RCLK, GPIO.OUT)
        GPIO.setup(SRCLK, GPIO.OUT)
        GPIO.output(SDI, GPIO.LOW)
        GPIO.output(RCLK, GPIO.LOW)
        GPIO.output(SRCLK, GPIO.LOW)
        
        #logging.info("Configuring GPIO_" + str(self.channelOut) + " as an output.")
        #GPIO.setup(self.channelOut, GPIO.OUT)

    def start(self):
        logging.info("Call to method 'start' from child class. Feature is implemented")
        super().start()
        
    def stop(self):
        logging.info("Call to method 'stop' from child class. Feature is implemented")
        super().stop()

