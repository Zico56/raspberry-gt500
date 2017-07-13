import logging
from tkinter import *
from PIL import Image, ImageTk
from Led import Led
from Gallery import Gallery
import GPIO
from GPIO import App
import GenericFeature
from GenericFeature import *
import configparser

config = configparser.RawConfigParser() #https://docs.python.org/2/library/configparser.html
config.read('config.properties')

####### LOGGER #######
# TODO
#logLevel = config.get('LOGGING', 'log.level')
logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.INFO)
logger = logging.getLogger('Application')

fenetre = Tk()

#Window without title and border
#fenetre.overrideredirect(1)

fenetre.wm_title("Rasperry GT500")

def createImage(imgPath):
    image = Image.open(imgPath)
    photoImage = ImageTk.PhotoImage(image)
    return photoImage

#---------------------------------------------------------------------------------

verticalPW = PanedWindow(fenetre, orient=VERTICAL, bg="black")

imgBg = createImage("png/shelby.png")
canvas = Canvas(width=350, height=200, bg="black", highlightthickness=0)
canvas.create_image(0, 0, anchor=NW, image=imgBg)
verticalPW.add(canvas)

#gallery = Gallery(fenetre)
#gallery.panel.place(relx=0.5, rely=0.4, anchor=CENTER)
#gallery.panel.focus_set()

frame = Frame(bg="black", bd=0)

####### for test 
#feature = GenericFeature("Test")
#print(str(type(feature)))
#feature.start()
#######

indicatorList = config.items("INDICATOR_PATH")
featureList = config.items("FEATURE_MODULE")
gridNumberOfColumns = len(indicatorList)
for x in range(0, gridNumberOfColumns):

    led = Led(frame)
    led.label.grid(row=0, column=x)

    feature = GenericFeature(fenetre, featureList[x][1], led)
    
    # for testing mode
    feature.setLedEventBinding()
    
    imgIndic = PhotoImage(file=indicatorList[x][1])
    indicator = Label(frame, image=imgIndic, bg="black")
    indicator.image = imgIndic
    indicator.grid(row=1, column=x)
    
    frame.columnconfigure(x, weight=20)

frame.pack()

verticalPW.add(frame)
verticalPW.pack()

fenetre.geometry('%dx%d+%d+%d' % (350, 295, 0, 0))

# for testing mode
#App()

fenetre.mainloop()


    

