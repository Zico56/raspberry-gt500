import logging
import threading
import time
from Configuration import config
from Configuration import testMode
from features.GpioFeature import *

if not testMode:
    from omxplayer import OMXPlayer

class VideoPlayer(GpioFeature):

    # Path to video to play
    path = config.get('VIDEO', 'PATH')

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)

    def start(self):
        logging.info("Video player start")
        super().start()
        if not testMode:
            self.player = OMXPlayer(self.path)
            self.thread = threading.Thread(target=self.checkEnd)
            self.thread.start()  
             
    def stop(self):
        logging.info("Video player stop")
        super().stop()
        if not testMode:
            self.player.quit()

    def checkEnd(self):
        while player.is_playing:
            time.sleep(1)  
        self.state = GenericFeature.STATE_OFF
        self.indicator.swithOff()
    