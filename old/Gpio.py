import logging
from GenericFeature import *
from Configuration import config

################# Raspberry / Emulator mode #################
isTestMode = config.getboolean('TESTING', 'gpio.emulator')
if(isTestMode):
    from GPIOTest import GPIO
else:
    from RPi import GPIO
#############################################################

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Gpio(GenericFeature):

    def __init__(self, parent, feature, led):
        super().__init__(parent, feature, led)
        #GPIO.setup(18, GPIO.OUT)

    def setBinding(self, channel):
        logging.debug("Configuring GPIO_" + str(channel) + "as input")
        GPIO.setup(channel, GPIO.IN)
        GPIO.add_event_detect(channel, GPIO.RISING, callback=self.processEvent, bouncetime=75)

    def start(self):
        self.led.swithOn()
        #GPIO.output(18, GPIO.HIGH)
        
    def stop(self):
        self.led.swithOff()
        #GPIO.output(18, GPIO.LOW)
