from GenericFeature import *

import configparser
config = configparser.RawConfigParser()
config.read('config.properties')
isTestMode = config.getboolean('TESTING', 'gpio.emulator')
if(isTestMode):
    from GPIOTest import GPIO
else:
    from RPi import GPIO

#logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.DEBUG)
#logger = logging.getLogger('Test')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Gpio(GenericFeature):

    def __init__(self, parent, feature, led):
        super().__init__(parent, feature, led)
        channel = 17
        GPIO.setup(channel, GPIO.IN)
        GPIO.add_event_detect(channel, GPIO.RISING, callback=self.processEvent, bouncetime=75) 
        #GPIO.setup(18, GPIO.OUT)


    def start(self):
        print("Call to method 'start' from child class. Feature is implemented")
        self.led.swithOn()
        #GPIO.output(18, GPIO.HIGH)
        
    def stop(self):
        print("Call to method 'stop' from child class. Feature is implemented")
        self.led.swithOff()
        #GPIO.output(18, GPIO.LOW)
