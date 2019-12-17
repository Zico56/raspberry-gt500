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
    'POSITION_LIGHTS': {
        1: 0x0811
    },
    'MAIN_LIGHTS': {    #front & tail lights, license plate, dashboard
        1: 0x3600
    },
    'FOG_LIGHTS': {
        1: 0x0100
    }, 
    'ROOF_LIGHT': {
        1: 0x4000
    },
    'REVERSE_LIGHT': {
        1: 0x8000
    },
    'TURN_INDICATORS': {
        1: [0x0003,0x0007,0x000f,0x0000,0x0000,0x0000], #Left
        2: [0x0030,0x0070,0x00f0,0x0000,0x0000,0x0000], #Right
        3: [0x00ff, 0x0000]                             #Warning
    }              
}
ALL_LIGHTS_OFF = 0x0000

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
        self.ledTemplate = ALL_LIGHTS_OFF
        self.setRegisterOutput()
        self.displayRegisterOutput()
        
        for lightModule in lightModules:  
            lightModulesMode[lightModule] = 0
            
    def setRegisterOutput(self):
        # Iteration on each 74HC595 bit/output
        #print(format(self.ledTemplate, '08b'))
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
        if not (lightModule in lightModules):
            lightModules.append(lightModule)
        lightModulesMode[lightModule] = moduleMode
    
    def unsetLightModule(self, lightModule):
        lightModules.remove(lightModule)
        lightModulesMode[lightModule] = 0
        
    def setTemplate(self):
        self.ledTemplate = ALL_LIGHTS_OFF
        self.sleeptime = 0.4
                                
        for lightModule in lightModules:
            moduleMode = lightModulesMode[lightModule]  
                   
            if (moduleMode != 0):                
                mask = lightModulesMask[lightModule][moduleMode]
                
                if (type(mask) == list):
                    maskId = lightModule + str(moduleMode)
                    
                    if (maskId in lightModulesSeqIdx):
                        maskIdx = lightModulesSeqIdx[maskId]
                        if (maskIdx == len(mask)-1):
                            maskIdx = 0
                        else:
                            maskIdx += 1
                    else:
                        maskIdx = 0
                        
                    mask = mask[maskIdx]
                    lightModulesSeqIdx[maskId] = maskIdx

                self.ledTemplate = self.ledTemplate ^ mask
        
        # Specific case for "turn indicators"
        if ('TURN_INDICATORS' in lightModules):
            #Modifying tempo for left/right indicators (for led chaser)
            if (lightModulesMode['TURN_INDICATORS']==1 or lightModulesMode['TURN_INDICATORS']==2):
                self.sleeptime = 0.1
            
            #Complementing bit 0 and 4 if "Position light" is on 
            #(otherwise, front lights are desynchronized because of the XOR mask)
            if ('POSITION_LIGHTS' in lightModules):
                if(moduleMode == 1):
                    self.ledTemplate = self.ledTemplate ^ 0x1
                elif(moduleMode == 2):
                    self.ledTemplate = self.ledTemplate ^ 0x4
                elif(moduleMode == 3):
                    self.ledTemplate = self.ledTemplate ^ 0x5
    
    def _74hc595(self):
        # Display template for leds
        self.setTemplate()
        
        logging.info("Led template: " + str(bin(self.ledTemplate)))
        
        self.setRegisterOutput()
        self.displayRegisterOutput()
                 
        # Time out delay between two sequence of the led template
        time.sleep(self.sleeptime)     

register = ShiftRegister()   
  
