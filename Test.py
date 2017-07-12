#from GenericFeature import *

#logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.DEBUG)
#logger = logging.getLogger('Test')

'''
class GenericFeature:

    def __new__(cls, classe):
        print("Appel de la methode __new__ de la classe")
        return object.__new__(classe)
    
    def __init__(self):
        self.led = ''
        self.indicator = ''

    def start(self, classe):
        print("Call to method from generic class. Not implemented for the required feature.")
    
    def stop(self):
        print("Call to method from generic class. Not implemented for the required feature.")

class Test(GenericFeature):

    def __init__(self):
        super().__init__()
        #self.state = STATE_OFF
        #self.led = ''
        #self.indicator = ''

    def start(self):
        print("Call to method from child class. Feature is implemented")
'''

class Test():

    def __init__(self):
        pass

    def start(self):
        print("Call to method from child class. Feature is implemented")

#test = object.__new__(Test)
#print("Type:" + str(type(test)))
#test = Test()
#test.start()
