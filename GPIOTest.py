import logging
import time
from tkinter import *
import tkinter as tk
from Configuration import config

dictionaryPins = {}
dictionaryPinsTkinter = {}

isExtendedGpio = config.getboolean('TESTING', 'gpio.extended')
if (isExtendedGpio):
    GPIONames=["14","15","18","23","24","25","8","7","12","16","20","21","2","3","4","17","27","22","10","9","11","5","6","13","19","26"]
else:
    GPIONames=["14","15","18","23","24","25","8","7","2","3","4","17","27","22","10","9","11"]



'''
def toggleButton(gpioID):
    objBtn = dictionaryPinsTkinter[str(gpioID)]
    objPin = dictionaryPins[str(gpioID)]
    
    if(objPin.In == "1"):
        objPin.In = "0"
    elif(objPin.In == "0"):
        objPin.In = "1"
        
    objBtn["text"] = "GPIO" + str(gpioID) + "\nIN=" + str(objPin.In)
'''
    
def buttonClick(self):
    channel = (self.widget.config('command')[-1])
    global dictionaryPinsTkinter
    objBtn = dictionaryPinsTkinter[str(channel)]
    objBtn["text"] = "GPIO" + str(channel) + "\nIN=" + str(PIN.UP)
    objBtn.callback(self)

def buttonRelease(self):
    channel = (self.widget.config('command')[-1])
    global dictionaryPinsTkinter
    objBtn = dictionaryPinsTkinter[str(channel)]
    objBtn["text"] = "GPIO" + str(channel) + "\nIN=" + str(PIN.DWN)
 
def drawGPIOIn(gpioID):
    global dictionaryPins
    global dictionaryPinsTkinter
    
    objPin = dictionaryPins[str(gpioID)]
    objBtn = dictionaryPinsTkinter[str(gpioID)]  
    
    objBtn.configure(relief='raised')
    objBtn.configure(bd="1px")
    objBtn["text"] = "GPIO" + str(gpioID) + "\nIN=" + str(objPin.state)

def drawGPIOOut(gpioID):
    global dictionaryPins
    global dictionaryPinsTkinter

    objPin = dictionaryPins[str(gpioID)]
    objBtn = dictionaryPinsTkinter[str(gpioID)]  

    if (objPin.mode != PIN.OUT):
        raise Exception("GPIO_" + str(gpioID) + " should be set as an output.")
    
    objBtn["text"] = "GPIO" + str(gpioID) + "\nOUT=" + str(objPin.state)

    objBtn.configure(state=DISABLED)
    objBtn.configure(disabledforeground='White')
    if (objPin.state == PIN.UP):
        objBtn.configure(background='DarkGreen')  
    elif (objPin.state == PIN.DWN):        
        objBtn.configure(background='FireBrick')
	
class App():

    def __init__(self):
        self.root = Toplevel()        
        self.root.wm_title("GPIO EMULATOR")        
        self.initGrid()

    def initGrid(self):	
        global dictionaryPinsTkinter
        
        ########### First row ###########    
            
        #5V
        pin2label = Label(self.root, text="5V", fg="red")
        pin2label.grid(row=0, column=0, padx=(10, 10))
        
        #5V
        pin4label = Label(self.root, text="5V", fg="red")
        pin4label.grid(row=0, column=1, padx=(10, 10))

        #GND
        pin6label = Label(self.root, text="GND", fg="black")
        pin6label.grid(row=0, column=2, padx=(10, 10))
        
        #GPIO14
        pin8btn = Button(self.root, text="GPIO14\nOUT=0", command="14", padx ="1px", pady="1px", bd="1px", fg="blue", activebackground="slategray")
        pin8btn.grid(row=0, column=3, padx=(10, 10),pady=(5,5))
        dictionaryPinsTkinter["14"] = pin8btn
   
        #GPIO15
        pin10btn = Button(self.root, text="GPIO15\nOUT=0", command="15", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin10btn.grid(row=0, column=4, padx=(10, 10))
        dictionaryPinsTkinter["15"] = pin10btn
 
        #GPIO18
        pin12btn = Button(self.root, text="GPIO18\nOUT=0", command="18",  padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin12btn.grid(row=0, column=5, padx=(10, 10))
        dictionaryPinsTkinter["18"] = pin12btn
        
        #GND
        pin14label = Label(self.root, text="GND", fg="black")
        pin14label.grid(row=0, column=6, padx=(10, 10))

        #GPIO23
        pin16btn = Button(self.root, text="GPIO23\nOUT=0", command="23", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin16btn.grid(row=0, column=7, padx=(10, 10))
        dictionaryPinsTkinter["23"] = pin16btn

        #GPIO24
        pin18btn = Button(self.root, text="GPIO24\nOUT=0",command="24",  padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin18btn.grid(row=0, column=8, padx=(10, 10))
        dictionaryPinsTkinter["24"] = pin18btn
      
        #GND
        pin20label = Label(self.root, text="GND", fg="black")
        pin20label.grid(row=0, column=9, padx=(10, 10))

        #GPIO25
        pin22btn = Button(self.root, text="GPIO25\nOUT=0", command="25", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin22btn.grid(row=0, column=10, padx=(10, 10))
        dictionaryPinsTkinter["25"] = pin22btn
        
        #GPIO08
        pin24btn = Button(self.root, text="GPIO8\nOUT=0", command="8", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin24btn.grid(row=0, column=11, padx=(10, 10))
        dictionaryPinsTkinter["8"] = pin24btn

        #GPIO07
        pin26btn = Button(self.root, text="GPIO7\nOUT=0", command="7",  padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin26btn.grid(row=0, column=12, padx=(10, 10))
        dictionaryPinsTkinter["7"] = pin26btn

        if (isExtendedGpio):
            #ID_SC
            pin28label = Label(self.root, text="ID_SC", fg="black")
            pin28label.grid(row=0, column=13, padx=(10, 10))

            #GND
            pin30label = Label(self.root, text="GND", fg="black")
            pin30label.grid(row=0, column=14, padx=(10, 10))

            #GPIO12
            pin32btn = Button(self.root, text="GPIO12\nOUT=0", command="12", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin32btn.grid(row=0, column=15, padx=(10, 10))
            dictionaryPinsTkinter["12"] = pin32btn

            #GND
            pin34label = Label(self.root, text="GND", fg="black")
            pin34label.grid(row=0, column=16, padx=(10, 10))

            #GPIO16
            pin36btn = Button(self.root, text="GPIO16\nOUT=0", command="16",  padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin36btn.grid(row=0, column=17, padx=(10, 10))
            dictionaryPinsTkinter["16"] = pin36btn

            #GPIO20
            pin38btn = Button(self.root, text="GPIO20\nOUT=0", command="20", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin38btn.grid(row=0, column=18, padx=(10, 10))
            dictionaryPinsTkinter["20"] = pin38btn
            
            #GPIO21
            pin40btn = Button(self.root, text="GPIO21\nOUT=0", command="21", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin40btn.grid(row=0, column=19, padx=(10, 10))
            dictionaryPinsTkinter["21"] = pin40btn

        ########### Second row
        
        #3V3
        pin1label = Label(self.root, text="3V3", fg="dark orange")
        pin1label.grid(row=1, column=0, padx=(10, 10), pady=(5,5))

        #GPIO02
        pin03btn = Button(self.root, text="GPIO2\nOUT=0",command="2", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin03btn.grid(row=1, column=1, padx=(10, 10),pady=(5,5))
        dictionaryPinsTkinter["2"] =pin03btn

        #GPIO03
        pin05btn = Button(self.root, text="GPIO3\nOUT=0", command="3", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin05btn.grid(row=1, column=2, padx=(10, 10))
        dictionaryPinsTkinter["3"] = pin05btn

        #GPIO04
        pin07btn = Button(self.root, text="GPIO4\nOUT=0", command="4", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin07btn.grid(row=1, column=3, padx=(10, 10))
        dictionaryPinsTkinter["4"] = pin07btn

        #GND
        pin09label = Label(self.root, text="GND", fg="black")
        pin09label.grid(row=1, column=4, padx=(10, 10))

        #GPIO17
        pin11btn = Button(self.root, text="GPIO17\nOUT=0", command="17", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin11btn.grid(row=1, column=5, padx=(10, 10))
        dictionaryPinsTkinter["17"] = pin11btn

        #GPIO27
        pin13btn = Button(self.root, text="GPIO27\nOUT=0", command="27", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin13btn.grid(row=1, column=6, padx=(10, 10))
        dictionaryPinsTkinter["27"] = pin13btn

        #GPIO22
        pin15btn = Button(self.root, text="GPIO22\nOUT=0", command="22", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin15btn.grid(row=1, column=7, padx=(10, 10))
        dictionaryPinsTkinter["22"] = pin15btn

        #3V3
        pin17label = Label(self.root, text="3V3", fg="dark orange")
        pin17label.grid(row=1, column=8, padx=(10, 10))

        #GPIO10
        pin19btn = Button(self.root, text="GPIO10\nOUT=0", command="10",  padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin19btn.grid(row=1, column=9, padx=(10, 10))
        dictionaryPinsTkinter["10"] = pin19btn

        #GPIO09
        pin21btn = Button(self.root, text="GPIO9\nOUT=0", command="9", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin21btn.grid(row=1, column=10, padx=(10, 10))
        dictionaryPinsTkinter["9"] = pin21btn

        #GPIO11
        pin23btn = Button(self.root, text="GPIO11\nOUT=0", command="11", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
        pin23btn.grid(row=1, column=11, padx=(10, 10))
        dictionaryPinsTkinter["11"] = pin23btn

        #GND
        pin25label = Label(self.root, text="GND", fg="black")
        pin25label.grid(row=1, column=12, padx=(10, 10))

        if (isExtendedGpio):
            #ID_SD
            pin27label = Label(self.root, text="ID_SD", fg="black")
            pin27label.grid(row=1, column=13, padx=(10, 10))

            #GPIO05
            pin29btn = Button(self.root, text="GPIO5\nOUT=0", command="5", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin29btn.grid(row=1, column=14, padx=(10, 10))
            dictionaryPinsTkinter["5"] = pin29btn

            #GPIO06
            pin31btn = Button(self.root, text="GPIO6\nOUT=0", command="6", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin31btn.grid(row=1, column=15, padx=(10, 10))
            dictionaryPinsTkinter["6"]=pin31btn

            #GPIO13
            pin33btn = Button(self.root, text="GPIO13\nOUT=0", command="13", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin33btn.grid(row=1, column=16, padx=(10, 10))
            dictionaryPinsTkinter["13"] = pin33btn

            #GPIO19
            pin35btn = Button(self.root, text="GPIO19\nOUT=0", command="19", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin35btn.grid(row=1, column=17, padx=(10, 10))
            dictionaryPinsTkinter["19"] = pin35btn   
                
            #GPIO26
            pin37btn = Button(self.root, text="GPIO26\nOUT=0", command="26", padx ="1px", pady="1px", bd="0px", fg="blue", activebackground="slategray")
            pin37btn.grid(row=1, column=18, padx=(10, 10))
            dictionaryPinsTkinter["26"] = pin37btn

            #GND
            pin39label = Label(self.root, text="GND", fg="black")
            pin39label.grid(row=1, column=19, padx=(10, 10))

class PIN():
    # Pin mode
    IN = 1
    OUT = 0
    NONE = -1
    
    # Pin state
    UP = 1
    DWN = 0
    
    #pull_up_down = "PUD_OFF" #PUD_UP/PUD_DOWN/PUD_OFF

    def __init__(self, mode=0, state=0):
        if (mode != PIN.IN) and (mode != PIN.OUT) and (mode != PIN.NONE):
            raise Exception("Unknown pin mode: " + str(mode))
    
        if (state != PIN.UP) and (state != PIN.DWN):
            raise Exception("Unknown pin state: " + str(state))
    
        self.mode = mode
        self.state = state
		
class GPIO:

    #constants
    LOW = 0 
    HIGH = 1
    OUT = 2
    IN = 3
    PUD_OFF = 4
    PUD_DOWN = 5
    PUD_UP = 6
    BCM = 7

    RISING=1
    FALLING=-1
    BOTH=0
    
    #flags
    setModeDone = False
    
    #Extra functions
    '''
    def checkModeValidator():
        if(GPIO.setModeDone == False):
            raise Exception('Setup your GPIO mode. Must be set to BCM')
    '''
    
    def checkChannelSetUpAndMode(channel, mode):
        channel = str(channel)
        
        global dictionaryPins
        if channel not in dictionaryPins:
            #if channel is not setup
            raise Exception('GPIO' + channel + ' has not been setup.')
            
        objPin = dictionaryPins[channel]
        if (objPin.mode != mode):
            raise Exception('GPIO' + channel + ' setup as ' + str(objPin.mode) + '. Must be setup as: ' + str(mode))
    
    #GPIO LIBRARY Functions
    def setmode(mode):
        #time.sleep(1)
        if(mode == GPIO.BCM):
            GPIO.setModeDone = True
        else:
            GPIO.setModeDone = False

    def setwarnings(flag):
        logging.warning("Test mode. Warning flag not implemented")
      
    def setup(channel, state, initial=-1, pull_up_down=-1):
        global dictionaryPins
        
        #GPIO.checkModeValidator()

        #check if provided channel exists		
        if str(channel) not in GPIONames:
            raise Exception('GPIO ' + str(channel) + ' does not exist')

        #check if channel is already setup
        if str(channel) in dictionaryPins:
            raise Exception('GPIO is already setup')

        #Set GPIO pin as an output (default OUT 0)
        if(state == GPIO.OUT):
            objTemp = PIN(mode=PIN.OUT)
            #if(initial == GPIO.HIGH):
            #    objTemp.Out = "1"
            objTemp.Out = "0"
                
            dictionaryPins[str(channel)] = objTemp
            drawGPIOOut(channel)
            
        #Set GPIO pin as an input
        elif(state == GPIO.IN):
            objTemp = PIN(mode=PIN.IN)
            #objTemp.In = "0"
            '''
            if(pull_up_down == -1) or (pull_up_down == GPIO.PUD_DOWN):
                objTemp.pull_up_down = "PUD_DOWN"
                objTemp.In = "0"
            elif(pull_up_down == GPIO.PUD_UP):
                objTemp.pull_up_down = "PUD_UP"
                objTemp.In = "1"
            '''
            
            dictionaryPins[str(channel)] = objTemp
            drawGPIOIn(channel)
            
    def output(channel, outmode):
        channel = str(channel)
        GPIO.checkChannelSetUpAndMode(channel, PIN.OUT)
        #GPIO.checkModeValidator()
                
        if (outmode != GPIO.LOW and outmode != GPIO.HIGH):
            raise Exception('Output must be set to HIGH/LOW')
        
        global dictionaryPinsTkinter
        objBtn = dictionaryPinsTkinter[channel]
        if(outmode == GPIO.LOW):
            objBtn.configure(background='FireBrick')
        elif(outmode == GPIO.HIGH):
            objBtn.configure(background='DarkGreen')

    def input(channel):        
        channel = str(channel)
        #GPIO.checkModeValidator()        
        GPIO.checkChannelSetUpAndMode(channel, PIN.IN)

        if (objPin.state == PIN.UP):
            return True
        elif (objPin.state == PIN.DWN):
            return False
	
    def cleanup():
        pass
        
    def add_event_detect(channel, edge, callback, bouncetime):
        global dictionaryPinsTkinter
        objBtn = dictionaryPinsTkinter[str(channel)]
        objBtn.bind("<Button-1>", buttonClick)
        objBtn.bind("<ButtonRelease-1>", buttonRelease)
        objBtn.callback = callback    
        '''
        if (edge == GPIO.RISING) or (edge == GPIO.BOTH):
            objBtn.bind("<Button-1>", buttonClick)
            objBtn.callback = callback

        if (edge == GPIO.FALLING) or (edge == GPIO.BOTH):
            objBtn.bind("<ButtonRelease-1>", buttonRelease)
            objBtn.callback = callback
        '''