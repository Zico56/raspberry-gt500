import logging
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from Led import Led
import GPIO
from GPIO import App

logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.INFO)
logger = logging.getLogger('Application')

fenetre = Tk()

#Window without title and border
#fenetre.overrideredirect(1)

fenetre.wm_title("Rasperry GT500")

gridNumberOfColumns = 5
ledTab = []
indicatorImgList = [
    "gif/rsz_voyant_phare1_off.gif",
    "gif/rsz_voyant_phare2_off.gif",
    "gif/rsz_voyant_phare3_off.gif",
    "gif/rsz_voyant_warning_off.gif",
    "gif/rsz_voyant_moteur_off.gif"]

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

frame = Frame(bg="black", bd=0)

for x in range(0, gridNumberOfColumns):
    #logging.info("We're on time %d" % (x))
    led = Led(frame)
    ledTab.append(led)
    
    #led.bind("<Button-1>", callbackMethodList[x])
    led.label.grid(row=0, column=x)
    
    #logging.info("img: " + indicatorImgList[x])
    imgIndic = PhotoImage(file=indicatorImgList[x])
    indicator = Label(frame, image=imgIndic, bg="black")
    indicator.image = imgIndic
    indicator.grid(row=1, column=x)
    
    frame.columnconfigure(x, weight=20)

frame.pack()

verticalPW.add(frame)
verticalPW.pack()

fenetre.geometry('%dx%d+%d+%d' % (350, 295, 0, 0))

'''
window = Toplevel()
window.geometry("200x200")
Label(window, text="this is window").pack()
'''
App()

fenetre.mainloop()


    

