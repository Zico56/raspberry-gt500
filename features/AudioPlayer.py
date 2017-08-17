import pygame
import logging
from Configuration import config
from features.GpioFeature import *

class AudioPlayer(GpioFeature):

    # Path to track to play
    path = config.get('AUDIO', 'PATH')

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(self.path)

    def start(self):
        logging.info("Audio player start")
        super().start()
        pygame.mixer.music.play()
        
    def stop(self):
        logging.info("Audio player stop")
        super().stop()
        pygame.mixer.music.stop()
