import logging
from Configuration import config
from features.GenericFeature import *

################# Raspberry / Emulator mode #################
if(testMode):
    from emulator.GPIOEmulator import GPIO
else:
    from RPi import GPIO
#############################################################

class GpioFeature(GenericFeature):

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)

    def setBinding(self):
        super().setBinding()  

        # GPIO input set up
        self.channelIn = self.featureOptions['GPIO_INPUT']        
        if (self.channelIn == None) or (self.channelIn == ''):
            raise Exception("No GPIO input defined.")            
        logging.info("Configuring GPIO_" + self.channelIn + " as an input.")
        self.channelIn = int(self.channelIn)
        GPIO.setup(int(self.channelIn), GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        # GPIO output set up
        if (config.has_option(self.configSection, 'GPIO_OUTPUT')):
            self.channelOut = self.featureOptions['GPIO_OUTPUT']           
            logging.info("Configuring GPIO_" + self.channelOut + " as an output.")
            self.channelOut = int(self.channelOut)
            GPIO.setup(int(self.channelOut), GPIO.OUT)
         
        # GPIO event set up
        GPIO.add_event_detect(self.channelIn, GPIO.RISING, callback=self.processEvent, bouncetime=75)
    
    def start(self): 
        if hasattr(self, 'channelOut'):
            GPIO.output(self.channelOut, GPIO.HIGH)
            print("out")
        else:
            print("pas out")
        
    def stop(self):
        if hasattr(self, 'channelOut'):
            GPIO.output(self.channelOut, GPIO.LOW)
