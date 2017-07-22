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

verticalPW = PanedWindow(fenetre, orient=VERTICAL, bg="black")

canvas = Canvas(width=350, height=200, bg="black", highlightthickness=0)
imgBg = createImage("png/shelby.png")
canvas.create_image(0, 0, anchor=NW, image=imgBg)
verticalPW.add(canvas)

frame = Frame(bg="black", bd=0)

indicatorList = config.items("INDICATOR_PATH")

featureList = config.items("FEATURE_MODULE")
nbFeature = len(indicatorList)
for x in range(0, nbFeature):

    led = Led(frame)
    led.label.grid(row=0, column=x)

    feature = GenericFeature(fenetre, featureList[x][1], led)
    
    channel = config.get('GPIO_INPUT', 'GPIO_IN_'+str(x+1))
    feature.setBinding(channel=channel)
    
    imgIndic = PhotoImage(file=indicatorList[x][1])
    indicator = Label(frame, image=imgIndic, bg="black")
    indicator.image = imgIndic
    indicator.grid(row=1, column=x)
    
    frame.columnconfigure(x, weight=20)

frame.pack()

verticalPW.add(frame)
verticalPW.pack()

fenetre.geometry('%dx%d+%d+%d' % (60*nbFeature, 295, 0, 0))

try:
    fenetre.mainloop()

except Exception as ex:
    traceback.print_exc()
finally:
    GPIO.cleanup() #this ensures a clean exit
    

