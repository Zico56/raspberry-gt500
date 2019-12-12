import logging
import time
import threading
from features.GpioFeature import *
from features.ShiftRegister import *

class ShiftRegisterFeature(GpioFeature):
    
    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        self.lightModule = self.featureOptions['LIGHT_MODULE']
        self.maxModeValue = int(self.featureOptions['MAX_MODE_VALUE'])
        self.modeValue = 0
            
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
        super().start()
        register.setLightModule(self.lightModule, self.modeValue)
        
    def stop(self):
        super().stop()
        register.unsetLightModule(self.lightModule)      