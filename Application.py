import logging
from tkinter import *

logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.DEBUG)

gridNumberOfColumns = 5
indicatorImgList = [
    "gif/rsz_voyant_phare1_off.png",
    "gif/rsz_voyant_phare2_off.png",
    "gif/rsz_voyant_phare3_off.png",
    "gif/rsz_voyant_warning_off.png",
    "gif/rsz_voyant_moteur_off.png"]
ledsState = {}

def callbackLed(event):
    imgOn = PhotoImage(file="gif/rsz_red-led-on-th.png")
    imgOff = PhotoImage(file="gif/rsz_red-led-off-th.png")
    
    state = ledsState[str(event.widget)]
    if ( state == "OFF"):
        event.widget.configure(image=imgOn)
        event.widget.image=imgOn
        ledsState[str(event.widget)] = "ON"
    elif ( state == "ON"):
        event.widget.configure(image=imgOff)
        event.widget.image=imgOff
        ledsState[str(event.widget)] = "OFF"
    else:
        raise Exception('Unknow led state')

def callback1(event):
    logging.info("callback 1")
    callbackLed(event)

def callback2(event):
    logging.info("callback 2")
    callbackLed(event)

def callback3(event):
    logging.info("callback 3")
    callbackLed(event)

def callback4(event):
    logging.info("callback 4")
    callbackLed(event)

def callback5(event):
    logging.info("callback 5") 
    callbackLed(event)    
    
callbackMethodList = [
    callback1,
    callback2,
    callback3,
    callback4,
    callback5]
 
def initLed(frame):
    img = PhotoImage(file="gif/rsz_red-led-off-th.png")
    led = Label(frame, image=img, bg="black")
    led.image = img
    #led.bind("<Button-1>", callbackLed)    
    ledsState[str(led)] = "OFF"
    return led
    
fenetre = Tk()
fenetre.wm_title("Rasperry GT500")

#Window without title and border
#fenetre.overrideredirect(1)

verticalPW = PanedWindow(fenetre, orient=VERTICAL, bg="black")

photo = PhotoImage(file="shelby.png")
canvas = Canvas(width=350, height=200, bg="black", highlightthickness=0)
canvas.create_image(0, 0, anchor=NW, image=photo)
verticalPW.add(canvas)

frame = Frame(bg="black", bd=0)

for x in range(0, gridNumberOfColumns):
    #logging.info("We're on time %d" % (x))
    led = initLed(frame)
    #callback = func = getattr(root, callbackMethodList[x]) 
    led.bind("<Button-1>", callbackMethodList[x])
    led.grid(row=0, column=x)
    
    #logging.info("img: " + indicatorImgList[x])
    imgIndic = PhotoImage(file=indicatorImgList[x])
    indicator = Label(frame, image=imgIndic, bg="black")
    indicator.image = imgIndic
    indicator.grid(row=1, column=x)
    
    frame.columnconfigure(x, weight=20)

verticalPW.add(frame)
verticalPW.pack()

fenetre.geometry('%dx%d+%d+%d' % (350, 295, 0, 0))
fenetre.mainloop()


