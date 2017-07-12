import logging

logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.DEBUG)
logger = logging.getLogger('GenericFeature')

class GenericFeature:

    STATE_ON = "ON"
    STATE_OFF = "OFF"
    
    def __new__(cls, module):
        print("Appel de la methode __new__ de la classe")
        #module_name = "Test"
        #class_name = "Test"
        print(module)
        imported = __import__(module)
        my_class = getattr(imported, module)
        #print(my_class)
        return object.__new__(my_class)
        #instance = my_class()
        #print("Type:" + str(type(instance)))
    
    def __init__(self, module):
        self.state = GenericFeature.STATE_OFF
        self.led = ''
        self.indicator = ''

    def start(self):
        logger.warning("Call to method from generic class. Not implemented for the required feature.")
    
    def stop(self):
        logger.warning("Call to method from generic class. Not implemented for the required feature.")