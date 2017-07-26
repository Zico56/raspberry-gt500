from tkinter import *
from PIL import Image, ImageTk

################# CONFIG #################
import logging
import logging.config
logging.config.fileConfig('properties/logging.properties')

from Configuration import config
from Configuration import testMode
##########################################

from Led import Led
from emulator.GPIOEmulator import App
from features.GenericFeature import *

def createImage(imgPath):
    image = Image.open(imgPath)
    photoImage = ImageTk.PhotoImage(image)
    return photoImage

fenetre = Tk()
fenetre.wm_title("Rasperry GT500")
#fenetre.overrideredirect(1) # ==> Window without title and border

######################## TEST MODE ########################
logging.debug("Test mode: " + str(testMode))
if(testMode):
    App()
###########################################################


# Init. frames
topFrame = Frame(fenetre, bg="black", bd=0)
topFrame.pack(side=TOP, fill='both', expand=True)

bottomFrame = Frame(fenetre, bg="black", bd=0)
bottomFrame.pack(side=BOTTOM, fill='both', expand=True)

# Background image
imgBg = createImage(config.get('APPLICATION', 'BKGND_IMG'))
canvas = Canvas(topFrame, width=350, height=200, bg="black", highlightthickness=0)
canvas.create_image(0, 0, anchor=NW, image=imgBg)
canvas.pack()

# Panel for led and indicator
horizontalPW = PanedWindow(bottomFrame, orient=HORIZONTAL, bg="black")
horizontalPW.pack()

# Adding feature
nbOfFeaturesMax = config.getint('APPLICATION', 'MAX_NB_OF_FEATURES')
nbOfFeaturesSet = 0
for x in range(1, nbOfFeaturesMax+1):
   
    configSection = 'FEATURE_' + str(x)
    if(config.has_section(configSection)):
        imgFrame = Frame(horizontalPW, bg="black", bd=0)
        imgFrame.pack()
    
        horizontalPW.add(imgFrame)
    
        feature = GenericFeature(imgFrame, configSection)     
        nbOfFeaturesSet+=1

# Configuring window size        
width = nbOfFeaturesSet*65   
if (width < 300):
    width = 300       
fenetre.geometry('%dx%d+%d+%d' % (width, 295, 0, 0))

try:
    fenetre.mainloop()

except Exception as ex:
    traceback.print_exc()
finally:
    GPIO.cleanup() #this ensures a clean exit
    

