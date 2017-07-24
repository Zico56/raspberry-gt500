import pygame
import os
import logging
from features.GenericFeature import *

class AudioPlayer(GenericFeature):

    

    def __init__(self, parent, feature, led):
        super().__init__(parent, feature, led)
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load("audio/SampleAudio_0.7mb.mp3")

    def start(self):
        logging.debug("Audio player start")
        pygame.mixer.music.play()
        
    def stop(self):
        logging.debug("Audio player stop")
        pygame.mixer.music.stop()
    
    def setBinding(self, **args):
        super().setBinding(**args)

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
