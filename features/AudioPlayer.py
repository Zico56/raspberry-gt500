import pygame
import logging
from Configuration import config
from features.GenericFeature import *

class AudioPlayer(GenericFeature):

    # Path to track to play
    path = config.get('PLAYER', 'PATH')

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(self.path)

    def start(self):
        logging.info("Audio player start")
        pygame.mixer.music.play()
        
    def stop(self):
        logging.info("Audio player stop")
        pygame.mixer.music.stop()
    
    def setBinding(self):
        super().setBinding()

'''
import os
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
