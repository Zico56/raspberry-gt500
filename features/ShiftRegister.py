import logging
import time
from Configuration import config
from Configuration import testMode
from CustomThread import *

################# Raspberry / Emulator mode #################
if(testMode):
    from emulator.GPIOEmulator import GPIO
else:
    from RPi import GPIO
#############################################################

lightModules = []
lightModulesSeqIdx = {}
lightModulesMode = {}
lightModulesMask = {
    'TURN_INDICATORS': {
        1: [0x0003,0x0004,0x0008],
        2: [0x0030,0x0040,0x0080],
        3: [0x0000,0x00ff],
    }, 
    'FOG_LIGHTS': {
        1: 0x0100
    }, 
    'POSITION_LIGHTS': {
        1: 0x0211
    }, 
    'MAIN_LIGHTS': {
        1: 0x3C00,
        2: 0x4C00
    }
}
NO_LIGHT = 0x0000

class ShiftRegister():   
        
    def __init__(self):
        logging.info("Initializing shift register 74HC595.")
        self.registerOptions = dict(config.items("SHIFT_REGISTER"))
        
        # Get GPIO port to use from configuration
        self.SDI = int(self.registerOptions['GPIO_SDI'])
        self.RCLK = int(self.registerOptions['GPIO_RCLK'])
        self.SRCLK = int(self.registerOptions['GPIO_SRCLK'])     

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
        
        self.resetRegister()

    def resetRegister(self):
        self.ledTemplate = NO_LIGHT
        self.setRegisterOutput()
        self.displayRegisterOutput()
        
        for lightModule in lightModules:  
            lightModulesMode[lightModule] = 0
            
    def setRegisterOutput(self):
        # Iteration on each 74HC595 bit/output
        for bit in range(0, 16):  
            # Masking and setting state for each 74HC595 output
            GPIO.output(self.SDI, 0x01 & (self.ledTemplate >> bit))
            GPIO.output(self.SRCLK, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(self.SRCLK, GPIO.LOW)
        
    def displayRegisterOutput(self):
        # Signal to 74HC595 for display output
        GPIO.output(self.RCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(self.RCLK, GPIO.LOW)

    def start(self):
        logging.info("Starting 74HC595 thread.")
        self.thread = CustomThread(self._74hc595)
        self.thread.event.clear()
        self.thread.start()
        
    def stop(self):
        logging.info("Reset shift register")
        self.resetRegister()
        lightModules = []
        logging.info("Stopping 74HC595 thread.")
        self.thread.event.set()  
       
    def setLightModule(self, lightModule, moduleMode):
        lightModules.append(lightModule)
        lightModulesMode[lightModule] = moduleMode
    
    def unsetLightModule(self, lightModule):
        lightModules.remove(lightModule)
        lightModulesMode[lightModule] = 0
        
    def setTemplate(self):
        self.ledTemplate = NO_LIGHT
        
        for lightModule in lightModules:
            moduleMode = lightModulesMode[lightModule]          
            if (moduleMode != 0):
                ledMask = lightModulesMask[lightModule][moduleMode]
                
                if (type(ledMask) == list):
                    idxKey = lightModule + str(moduleMode)
                    
                    if (idxKey in lightModulesSeqIdx):
                        seqIdx = lightModulesSeqIdx[idxKey]
                        if (seqIdx == len(ledMask)-1):
                            seqIdx = 0
                        else:
                            seqIdx += 1
                    else:
                        seqIdx = 0
                        
                    ledMask = ledMask[seqIdx]
                    lightModulesSeqIdx[idxKey] = seqIdx

                self.ledTemplate = self.ledTemplate ^ ledMask
    
    def _74hc595(self):
        # Display template for leds
        self.setTemplate()
        
        self.setRegisterOutput()
        self.displayRegisterOutput()
            
        # Time out delay between two sequence of the led template
        sleeptime = 0.5
        time.sleep(sleeptime)     

register = ShiftRegister()   
  
