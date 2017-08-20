import logging
import time
import threading
from features.GenericFeature import *
from features.ShiftRegister import *

class ShiftRegisterFeature(GenericFeature):
    
    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        self.lightModule = self.featureOptions['LIGHT_MODULE']
        self.maxModeValue = int(self.featureOptions['MAX_MODE_VALUE'])
        self.modeValue = 0
        
    def setBinding(self):
        super().setBinding()   
        
        # GPIO input set up
        self.channelIn = self.featureOptions['GPIO_INPUT']        
        if (self.channelIn == None) or (self.channelIn == ''):
            raise Exception("No GPIO input defined.")            
        logging.info("Configuring GPIO_" + self.channelIn + " as an input.")
        self.channelIn = int(self.channelIn)
        GPIO.setup(int(self.channelIn), GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # GPIO event set up
        GPIO.add_event_detect(self.channelIn, GPIO.RISING, callback=self.processEvent, bouncetime=75)
        
    # Override methods
    def processEvent(self, event):
        if (self.state == GenericFeature.STATE_OFF):
            self.modeValue = 1
            super().processEvent(event)
        else:
            if (self.modeValue == self.maxModeValue):
                self.modeValue = 0
                super().processEvent(event)
            else:
                self.modeValue += 1
                self.start()

    def start(self):
        register.setLightModule(self.lightModule, self.modeValue)
        
    def stop(self):
        register.unsetLightModule(self.lightModule)    
      
    '''
    thread = threading.Thread(target=self.blink)
    thread.start()  
    def blink(self):
        self.led.swithOff()
        time.sleep(0.1)
        self.led.swithOn()
    '''
  