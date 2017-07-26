import logging
import threading
import time
from Configuration import config
from features.GenericFeature import *

################# Raspberry / Emulator mode #################
if(testMode):
    from emulator.GPIOEmulator import GPIO
else:
    from RPi import GPIO
#############################################################

thread = None
pill2kill = threading.Event()

class ShiftRegister(GenericFeature):

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        
    def setBinding(self):
        super().setBinding()    
        
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
        logging.info("Call to method 'start' from child class. Feature is implemented")
        global thread
        thread = threading.Thread(target=self.demoMode, args=(pill2kill,))
        print("thread not alive")
        print("starting thread")
        thread.start()
        
    def stop(self):
        logging.info("Call to method 'stop' from child class. Feature is implemented")
        global thread
        print("alive: " + str(thread.isAlive()))
        print("thread alive")
        print("killing thread")
        pill2kill.set()
        thread.join()
        thread = None
        pill2kill.clear()

    '''
    def hc595_in(dat):
        for bit in range(0, 8):    
            GPIO.output(SDI, 0x80 & (dat << bit))
            GPIO.output(SRCLK, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(SRCLK, GPIO.LOW)
    
    def hc595_out():
        GPIO.output(RCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(RCLK, GPIO.LOW)
    '''
     
    def demoMode(self, stop_event):
        print("start demo mode")  
        t = threading.currentThread()
        while not stop_event.wait(1):
            print("demo mode")
        print("stop demo mode")        
    