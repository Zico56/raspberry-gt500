from tkinter import *
fenetre = Tk()

######################### CONFIG ##########################
import logging
import logging.config
logging.config.fileConfig('properties/logging.properties') 

from Configuration import config
from Configuration import testMode
###########################################################

################ Raspberry / Emulator mode ################
logging.info("GPIO Emulator: " + str(testMode))
if (testMode):
    from emulator.GPIOEmulator import App
    from emulator.GPIOEmulator import GPIO
    app = App()
else:
    from RPi import GPIO
###########################################################

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import time
from PIL import Image, ImageTk
from features.GenericFeature import *
from features.ShiftRegister import register

def createImage(imgPath):
    image = Image.open(imgPath)
    photoImage = ImageTk.PhotoImage(image)
    return photoImage

def shutdown(channel):  
    logging.info("shutdown")
    #os.system("sudo shutdown -h now") 

# GPIO for power function
gpioStop = int(config.get('APPLICATION', 'GPIO_STOP'))
GPIO.setup(gpioStop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(gpioStop, GPIO.RISING, callback=shutdown, bouncetime=75)

fenetre.wm_title("Rasperry GT500")
if not testMode:
    fenetre.overrideredirect(1) # ==> Window without title and border
    fenetre.attributes('-fullscreen', 1)

# Init. frames
topFrame = Frame(fenetre, bg="black", bd=0)
topFrame.pack(side=TOP, fill='both', expand=True)

bottomFrame = Frame(fenetre, bg="black", bd=0)
bottomFrame.pack(side=BOTTOM, fill='both', expand=True)

# Background image
imgBg = createImage(config.get('APPLICATION', 'BKGND_IMG'))
canvas = Canvas(topFrame, width=600, height=340, bg="black", highlightthickness=0)
canvas.create_image(0, 0, anchor=NW, image=imgBg)
canvas.pack()

# Panel for led and indicator
horizontalPW = PanedWindow(bottomFrame, height=140, orient=HORIZONTAL, bg="black")
horizontalPW.pack(expand=True)

#Init register
register.start()

# Adding feature
nbOfFeaturesMax = config.getint('APPLICATION', 'MAX_NB_OF_FEATURES')
nbOfFeaturesSet = 0

#######################################
def getlist(option, sep=','):
    list = []
    for chunk in option.split(sep):
        if(chunk != ''):
            list.append(chunk)
    return list
#######################################

windowWidth = 800
paneWidth = (windowWidth-30)//7
for x in range(1, nbOfFeaturesMax+1):
   
    configSection = 'FEATURE_' + str(x)
    if(config.has_section(configSection)):      
        imgFrame = Frame(horizontalPW, bg="black", bd=0, width=paneWidth)
        imgFrame.pack_propagate(False)  
        horizontalPW.add(imgFrame)
    
        feature = GenericFeature(imgFrame, configSection)     
        nbOfFeaturesSet += 1

# Configuring window size              
fenetre.geometry('%dx%d+%d+%d' % (800, 480, 0, 0))

try:
    fenetre.mainloop()
except Exception as ex:
    traceback.print_exc()
    logging.error(ex)
finally:
    register.stop()
    #time.sleep(2)
    GPIO.cleanup() #this ensures a clean exit
    

