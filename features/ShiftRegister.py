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
    
    LEDX = [0x00,0x18,0x24,0x42,0x81,0x42,0x24,0x18]
    LED0 = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]    #original mode
    LED1 = [0x01,0x03,0x07,0x0f,0x1f,0x3f,0x7f,0xff]    #blink mode 1
    LED2 = [0x01,0x05,0x15,0x55,0xb5,0xf5,0xfb,0xff]    #blink mode 2
    LED3 = [0x02,0x03,0x0b,0x0f,0x2f,0x3f,0xbf,0xff]    #blink mode 3

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
        global thread
        thread = threading.Thread(target=self.loop, args=(pill2kill,))
        logging.info("Starting 74HC595 thread.")
        thread.start()
        
    def stop(self):
        global thread
        logging.info("Killing 74HC595 thread.")
        pill2kill.set()
        thread.join()
        
        # Reinit thread and event for next time
        thread = None
        pill2kill.clear()

    def hc595_in(self, dat):
        #logging.info("Setting 74HC595 output")
        for bit in range(0, 8):    
            GPIO.output(self.SDI, 0x01 & (dat >> bit))
            GPIO.output(self.SRCLK, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(self.SRCLK, GPIO.LOW)
    
    def hc595_out(self):
        #logging.info("Flushing 74HC595 output")
        GPIO.output(self.RCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(self.RCLK, GPIO.LOW)

    def loop(self, stop_event):
        ledTemplate = self.LEDX
        sleeptime = 0.1
        while not stop_event.wait(1):
            for i in range(0, len(ledTemplate)):
                self.hc595_in(ledTemplate[i])
                self.hc595_out()
                time.sleep(sleeptime)
     
    '''
    def demoMode(self, stop_event):
        print("start demo mode")  
        t = threading.currentThread()
        while not stop_event.wait(1):
            print("demo mode")
        print("stop demo mode")  
    '''      
    