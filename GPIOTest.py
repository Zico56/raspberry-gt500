import time
from TypeChecker import typeassert
from tkinter import *
import tkinter as tk

dictionaryPins = {}
dictionaryPinsTkinter = {}

GPIONames=["14","15","18","23","24","25","8","7","12","16","20","21","2","3","4","17","27","22","10","9","11","5","6","13","19","26"]

'''
def drawGPIOOut(gpioID):
    global dictionaryPins
    global dictionaryPinsTkinter

    gpioID = str(gpioID)
    objPin = dictionaryPins[gpioID]
    objBtn = dictionaryPinsTkinter[gpioID]   

    if(objPin.SetMode == "OUT"):
        objBtn["text"] = "GPIO" + str(gpioID) + "\nOUT=" + str(objPin.Out)
        if(str(objPin.Out) == "1"):
            objBtn.configure(background='tan2')
            objBtn.configure(activebackground='tan2')
        else:
            objBtn.configure(background='DarkOliveGreen3')
            objBtn.configure(activebackground='DarkOliveGreen3')
'''

'''
def toggleButton(gpioID):
    objBtn = dictionaryPinsTkinter[str(gpioID)]
    objPin = dictionaryPins[str(gpioID)]
    
    if(objPin.In == "1"):
        objPin.In = "0"
    elif(objPin.In == "0"):
        objPin.In = "1"
        
    objBtn["text"] = "GPIO" + str(gpioID) + "\nIN=" + str(objPin.In)
        
def buttonClick(self):
    gpioID = (self.widget.config('command')[-1])
    toggleButton(gpioID)
'''
 
def drawGPIOIn(gpioID,In):
    global dictionaryPinsTkinter
    objBtn = dictionaryPinsTkinter[gpioID]
    objBtn.configure(background='gainsboro')
    objBtn.configure(activebackground='gainsboro')
    objBtn.configure(relief='raised')
    objBtn.configure(bd="1px")
    objBtn["text"] = "GPIO" + str(gpioID) + "\nIN=" + str(In)
    #objBtn.bind("<Button-1>", buttonClick)
    #objBtn.bind("<ButtonRelease-1>", buttonClickRelease)
			
class App():

    def __init__(self):
        self.root = Toplevel()
        
        self.root.wm_title("GPIO EMULATOR")
        self.root.geometry('%dx%d+%d+%d' % (1300, 100, 0, 0))
        
        self.initGrid()
        
        pin2label = Label(self.root, text="5V", fg="red")
        pin2label.grid(row=0, column=0, padx=(10, 10))
        
        Label(self.root, text="this is window")

    '''
    def callback(self):
        self.root.quit()
    '''

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
        pin8btn = Button(self.root, text="GPIO14\nOUT=0", command="14", padx ="1px", pady="1px", bd="1px", fg="blue", activeforeground="blue")
        pin8btn.grid(row=0, column=3, padx=(10, 10),pady=(5,5))
        dictionaryPinsTkinter["14"] = pin8btn

        #GPIO15
        pin10btn = Button(self.root, text="GPIO15\nOUT=0", command="15", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin10btn.grid(row=0, column=4, padx=(10, 10))
        dictionaryPinsTkinter["15"] = pin10btn
 
        #GPIO18
        pin12btn = Button(self.root, text="GPIO18\nOUT=0", command="18",  padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin12btn.grid(row=0, column=5, padx=(10, 10))
        dictionaryPinsTkinter["18"] = pin12btn
        
        #GND
        pin14label = Label(self.root, text="GND", fg="black")
        pin14label.grid(row=0, column=6, padx=(10, 10))

        #GPIO23
        pin16btn = Button(self.root, text="GPIO23\nOUT=0", command="23", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin16btn.grid(row=0, column=7, padx=(10, 10))
        dictionaryPinsTkinter["23"] = pin16btn

        #GPIO24
        pin18btn = Button(self.root, text="GPIO24\nOUT=0",command="24",  padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin18btn.grid(row=0, column=8, padx=(10, 10))
        dictionaryPinsTkinter["24"] = pin18btn
      
        #GND
        pin20label = Label(self.root, text="GND", fg="black")
        pin20label.grid(row=0, column=9, padx=(10, 10))

        #GPIO25
        pin22btn = Button(self.root, text="GPIO25\nOUT=0", command="25", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin22btn.grid(row=0, column=10, padx=(10, 10))
        dictionaryPinsTkinter["25"] = pin22btn
        
        #GPIO08
        pin24btn = Button(self.root, text="GPIO8\nOUT=0", command="8", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin24btn.grid(row=0, column=11, padx=(10, 10))
        dictionaryPinsTkinter["8"] = pin24btn

        #GPIO07
        pin26btn = Button(self.root, text="GPIO7\nOUT=0", command="7",  padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin26btn.grid(row=0, column=12, padx=(10, 10))
        dictionaryPinsTkinter["7"] = pin26btn

        #ID_SC
        pin28label = Label(self.root, text="ID_SC", fg="black")
        pin28label.grid(row=0, column=13, padx=(10, 10))

        #GND
        pin30label = Label(self.root, text="GND", fg="black")
        pin30label.grid(row=0, column=14, padx=(10, 10))

        #GPIO12
        pin32btn = Button(self.root, text="GPIO12\nOUT=0", command="12", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin32btn.grid(row=0, column=15, padx=(10, 10))
        dictionaryPinsTkinter["12"] = pin32btn

        #GND
        pin34label = Label(self.root, text="GND", fg="black")
        pin34label.grid(row=0, column=16, padx=(10, 10))

        #GPIO16
        pin36btn = Button(self.root, text="GPIO16\nOUT=0", command="16",  padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin36btn.grid(row=0, column=17, padx=(10, 10))
        dictionaryPinsTkinter["16"] = pin36btn

        #GPIO20
        pin38btn = Button(self.root, text="GPIO20\nOUT=0", command="20", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin38btn.grid(row=0, column=18, padx=(10, 10))
        dictionaryPinsTkinter["20"] = pin38btn
        
        #GPIO21
        pin40btn = Button(self.root, text="GPIO21\nOUT=0", command="21", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin40btn.grid(row=0, column=19, padx=(10, 10))
        dictionaryPinsTkinter["21"] = pin40btn

        ########### Second row
        
        #3V3
        pin1label = Label(self.root, text="3V3", fg="dark orange")
        pin1label.grid(row=1, column=0, padx=(10, 10), pady=(5,5))

        #GPIO02
        pin03btn = Button(self.root, text="GPIO2\nOUT=0",command="2", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin03btn.grid(row=1, column=1, padx=(10, 10),pady=(5,5))
        dictionaryPinsTkinter["2"] =pin03btn

        #GPIO03
        pin05btn = Button(self.root, text="GPIO3\nOUT=0", command="3", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin05btn.grid(row=1, column=2, padx=(10, 10))
        dictionaryPinsTkinter["3"] = pin05btn

        #GPIO04
        pin07btn = Button(self.root, text="GPIO4\nOUT=0", command="4", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin07btn.grid(row=1, column=3, padx=(10, 10))
        dictionaryPinsTkinter["4"] = pin07btn

        #gnd
        pin09label = Label(self.root, text="GND", fg="black")
        pin09label.grid(row=1, column=4, padx=(10, 10))

        #GPIO17
        pin11btn = Button(self.root, text="GPIO17\nOUT=0", command="17", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin11btn.grid(row=1, column=5, padx=(10, 10))
        dictionaryPinsTkinter["17"] = pin11btn

        #GPIO27
        pin13btn = Button(self.root, text="GPIO27\nOUT=0", command="27", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin13btn.grid(row=1, column=6, padx=(10, 10))
        dictionaryPinsTkinter["27"] = pin13btn

        #GPIO22
        pin15btn = Button(self.root, text="GPIO22\nOUT=0", command="22", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin15btn.grid(row=1, column=7, padx=(10, 10))
        dictionaryPinsTkinter["22"] = pin15btn

        #3V3
        pin17label = Label(self.root, text="3V3", fg="dark orange")
        pin17label.grid(row=1, column=8, padx=(10, 10))

        #GPIO10
        pin19btn = Button(self.root, text="GPIO10\nOUT=0", command="10",  padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin19btn.grid(row=1, column=9, padx=(10, 10))
        dictionaryPinsTkinter["10"] = pin19btn

        #GPIO09
        pin21btn = Button(self.root, text="GPIO9\nOUT=0", command="9", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin21btn.grid(row=1, column=10, padx=(10, 10))
        dictionaryPinsTkinter["9"] = pin21btn

        #GPIO11
        pin23btn = Button(self.root, text="GPIO11\nOUT=0", command="11", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin23btn.grid(row=1, column=11, padx=(10, 10))
        dictionaryPinsTkinter["11"] = pin23btn

        #GND
        pin25label = Label(self.root, text="GND", fg="black")
        pin25label.grid(row=1, column=12, padx=(10, 10))

        #ID_SD
        pin27label = Label(self.root, text="ID_SD", fg="black")
        pin27label.grid(row=1, column=13, padx=(10, 10))

        #GPIO05
        pin29btn = Button(self.root, text="GPIO5\nOUT=0", command="5", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin29btn.grid(row=1, column=14, padx=(10, 10))
        dictionaryPinsTkinter["5"] = pin29btn

        #GPIO06
        pin31btn = Button(self.root, text="GPIO6\nOUT=0", command="6", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin31btn.grid(row=1, column=15, padx=(10, 10))
        dictionaryPinsTkinter["6"]=pin31btn

        #GPIO13
        pin33btn = Button(self.root, text="GPIO13\nOUT=0", command="13", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin33btn.grid(row=1, column=16, padx=(10, 10))
        dictionaryPinsTkinter["13"] = pin33btn

        #GPIO19
        pin35btn = Button(self.root, text="GPIO19\nOUT=0", command="19", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin35btn.grid(row=1, column=17, padx=(10, 10))
        dictionaryPinsTkinter["19"] = pin35btn   
            
        #GPIO26
        pin37btn = Button(self.root, text="GPIO26\nOUT=0", command="26", padx ="1px", pady="1px", bd="0px", fg="blue", relief="sunken", activeforeground="blue")
        pin37btn.grid(row=1, column=18, padx=(10, 10))
        dictionaryPinsTkinter["26"] = pin37btn

        #GND
        pin39label = Label(self.root, text="GND", fg="black")
        pin39label.grid(row=1, column=19, padx=(10, 10))

class PIN():
    mode = "None" #IN/OUT/NONE
    stateOut = "0"
    #pull_up_down = "PUD_OFF" #PUD_UP/PUD_DOWN/PUD_OFF
    In = "1"

    def __init__(self, mode):
        self.mode = mode
        self.stateOut = "0"
		
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
    
    #GPIO LIBRARY Functions
    #@typeassert(int)
    def setmode(mode):
        #time.sleep(1)
        if(mode == GPIO.BCM):
            GPIO.setModeDone = True
        else:
            GPIO.setModeDone = False

    #@typeassert(bool)
    def setwarnings(flag):
        print("Test mode. Warning flag not implemented")
        pass

    #@typeassert(int,int,int,int)        
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
            objTemp = PIN("OUT")
            if(initial == GPIO.HIGH):
                objTemp.Out = "1"
                
            dictionaryPins[str(channel)] = objTemp
            drawGPIOOut(channel)
            
		#Set GPIO pin as an input
        elif(state == GPIO.IN):
            objTemp = PIN("IN")
            objTemp.In = "0"
            '''
            if(pull_up_down == -1) or (pull_up_down == GPIO.PUD_DOWN):
                objTemp.pull_up_down = "PUD_DOWN"
                objTemp.In = "0"
            elif(pull_up_down == GPIO.PUD_UP):
                objTemp.pull_up_down = "PUD_UP"
                objTemp.In = "1"
            '''
            
            dictionaryPins[str(channel)] = objTemp
            drawGPIOIn(str(channel), objTemp.In)
            
    #@typeassert(int,int)
    '''
    def output(channel, outmode):
        global dictionaryPins
        channel = str(channel)
        
        GPIO.checkModeValidator()

        if channel not in dictionaryPins:
            #if channel is not setup
            raise Exception('GPIO must be setup before used')
        else:
            objPin = dictionaryPins[channel]
            if(objPin.SetMode == "IN"):
                #if channel is setup as IN and used as an OUTPUT
                raise Exception('GPIO must be setup as OUT')

        
        if(outmode != GPIO.LOW and outmode != GPIO.HIGH):
            raise Exception('Output must be set to HIGH/LOW')
            
        objPin = dictionaryPins[channel]
        if(outmode == GPIO.LOW):
            objPin.Out = "0"
        elif(outmode == GPIO.HIGH):
            objPin.Out = "1"
        
        drawGPIOOut(channel)
    '''

    #@typeassert(int)
    '''
    def input(channel):
        global dictionaryPins
        channel = str(channel)

        GPIO.checkModeValidator()

        if channel not in dictionaryPins:
            #if channel is not setup
            raise Exception('GPIO must be setup before used')
        else:
            objPin = dictionaryPins[channel]
            if(objPin.SetMode == "OUT"):
                #if channel is setup as OUTPUT and used as an INPUT
                raise Exception('GPIO must be setup as IN')

        objPin = dictionaryPins[channel]
        if(objPin.In == "1"):
            return True
        elif(objPin.Out == "0"):
            return False
    '''
	
    def cleanup():
        pass
        
    def add_event_detect(channel, edge, callback, bouncetime):
        global dictionaryPinsTkinter
        objBtn = dictionaryPinsTkinter[str(channel)]
        objBtn.bind("<Button-1>", callback)