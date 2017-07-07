import logging
from tkinter import *
#import gobject
#import gst

logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename='application.log', level=logging.DEBUG)

ledsState = {}

'''
def callbackButton(event):
    #print("Button clicked: ", event.widget['text'])
    logging.info("Button clicked: "+event.widget['text'])
'''

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
    
def initLed(frame):
    img = PhotoImage(file="gif/rsz_red-led-off-th.png")
    led = Label(frame, image=img, bg="black")
    led.image = img
    led.bind("<Button-1>", callbackLed)
    ledsState[str(led)] = "OFF"
    return led
    
    
fenetre = Tk()
fenetre.wm_title("Rasperry GT500")

#Window without title and border
#fenetre.overrideredirect(1)

verticalPW = PanedWindow(fenetre, orient=VERTICAL, bg="black")
#verticalPW.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)

photo = PhotoImage(file="shelby.png")
canvas = Canvas(width=350, height=200, bg="black", highlightthickness=0)
canvas.create_image(0, 0, anchor=NW, image=photo)
verticalPW.add(canvas)

frame = Frame(bg="black", bd=0)

led1 = initLed(frame)
led1.grid(row=0, column=0)

led2 = initLed(frame)
led2.grid(row=0, column=1)

led3 = initLed(frame)
led3.grid(row=0, column=2)

led4 = initLed(frame)
led4.grid(row=0, column=3)

led5 = initLed(frame)
led5.grid(row=0, column=4)

imgIndic1 = PhotoImage(file="gif/rsz_voyant_phare1_off.png")
indicator1 = Label(frame, image=imgIndic1, bg="black")
indicator1.grid(row=1, column=0)

imgIndic2 = PhotoImage(file="gif/rsz_voyant_phare2_off.png")
indicator2 = Label(frame, image=imgIndic2, bg="black")
indicator2.grid(row=1, column=1)

imgIndic3 = PhotoImage(file="gif/rsz_voyant_phare3_off.png")
indicator3 = Label(frame, image=imgIndic3, bg="black")
indicator3.grid(row=1, column=2)

imgIndic4 = PhotoImage(file="gif/rsz_voyant_warning_off.png")
indicator4 = Label(frame, image=imgIndic4, bg="black")
indicator4.grid(row=1, column=3)

imgIndic5 = PhotoImage(file="gif/rsz_voyant_moteur_off.png")
indicator5 = Label(frame, image=imgIndic5, bg="black")
indicator5.grid(row=1, column=4)

'''
btn1 = Button(frame, text="Btn 1", command="14", padx ="1px", pady="1px", bd="1px", fg="blue", activeforeground="blue")
btn1.grid(row=1, column=0)
btn1.bind("<Button-1>", callbackButton)

btn2 = Button(frame, text="Btn 2", command="14", padx ="1px", pady="1px", bd="1px", fg="blue", activeforeground="blue")
btn2.grid(row=1, column=1)
btn2.bind("<Button-1>", callbackButton)

btn3 = Button(frame, text="Btn 3", command="14", padx ="1px", pady="1px", bd="1px", fg="blue", activeforeground="blue")
btn3.grid(row=1, column=2)
btn3.bind("<Button-1>", callbackButton)

btn4 = Button(frame, text="Btn 4", command="14", padx ="1px", pady="1px", bd="1px", fg="blue", activeforeground="blue")
btn4.grid(row=1, column=3)
btn4.bind("<Button-1>", callbackButton)

btn5 = Button(frame, text="Btn 5", command="14", padx ="1px", pady="1px", bd="1px", fg="blue", activeforeground="blue")
btn5.grid(row=1, column=4)
btn5.bind("<Button-1>", callbackButton)
'''

frame.columnconfigure(0, weight=20)
frame.columnconfigure(1, weight=20)
frame.columnconfigure(2, weight=20)
frame.columnconfigure(3, weight=20)
frame.columnconfigure(4, weight=20)

verticalPW.add(frame)
verticalPW.pack()

fenetre.geometry('%dx%d+%d+%d' % (350, 295, 0, 0))
fenetre.mainloop()


