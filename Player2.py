from tkinter import *
 
import pygame
import os

root = Tk()

def play():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load("audio/SampleAudio_0.7mb.mp3")
    pygame.mixer.music.play()

play()

root.mainloop()

''' 
def playpause():
    movie.pause()
 
root = Tk()
embed = Frame(root, width=640, height=480)
embed.grid(row=0,column=0)
playpausebutton=Button(root, command=playpause, text="Play/Pause")
playpausebutton.grid(row=1,column=0)
 
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
 
pygame.display.init()
screen = pygame.display.set_mode((640,480))
movie = pygame.movie.Movie('video/sample/mp4')
 
movie.play()
root.mainloop()
'''
