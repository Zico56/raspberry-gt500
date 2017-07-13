import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk

'''
import cv2

cap = cv2.VideoCapture("v2.mp4")
ret, frame = cap.read()
while(1):
   ret, frame = cap.read()
   cv2.imshow('frame',frame)
   if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
       cap.release()
       cv2.destroyAllWindows()
       break
   cv2.imshow('frame',frame)
'''

'''
import cv

vidFile = cv.CaptureFromFile( '/home/mhughes/sintel_trailer-480p.mp4' )

nFrames = int(  cv.GetCaptureProperty( vidFile, cv.CV_CAP_PROP_FRAME_COUNT ) )
fps = cv.GetCaptureProperty( vidFile, cv.CV_CAP_PROP_FPS )
waitPerFrameInMillisec = int( 1/fps * 1000/1 )

print 'Num. Frames = ', nFrames
print 'Frame Rate = ', fps, ' frames per sec'

for f in xrange( nFrames ):
  frameImg = cv.QueryFrame( vidFile )
  cv.ShowImage( "My Video Window",  frameImg )
  cv.WaitKey( waitPerFrameInMillisec  )

# When playing is done, delete the window
#  NOTE: this step is not strictly necessary, 
#         when the script terminates it will close all windows it owns anyways
cv.DestroyWindow( "My Video Window" )
'''

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture("video/sample.mp4")

def show_frame():
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 1)
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame) 

#Slider window (slider controls stage position)
'''
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)
'''

show_frame()  #Display 2
window.mainloop()  #Starts GUI